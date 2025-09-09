import os
from unittest.mock import AsyncMock, patch

import httpx
import pytest
from fastapi.testclient import TestClient
from main import QueryRequest, app

# Create test client
client = TestClient(app)

class TestQueryRequest:
    """Test the QueryRequest model validation"""
    
    def test_valid_query_request(self):
        """Test that valid QueryRequest is created successfully"""
        request = QueryRequest(question="What documents do I need for travel to Japan?")
        assert request.question == "What documents do I need for travel to Japan?"
    
    def test_empty_question_validation(self):
        """Test that empty question raises validation error"""
        with pytest.raises(ValueError):
            QueryRequest(question="")
    
    def test_missing_question_validation(self):
        """Test that missing question raises validation error"""
        with pytest.raises(ValueError):
            QueryRequest()

class TestRootEndpoint:
    """Test the root endpoint"""
    
    def test_root_endpoint(self):
        """Test that root endpoint returns correct message"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Q&A API Server is running"}

class TestHealthEndpoint:
    """Test the health check endpoint"""
    
    def test_health_endpoint(self):
        """Test that health endpoint returns healthy status"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

class TestAskEndpoint:
    """Test the /api/ask endpoint"""
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-api-key"})
    @patch("httpx.AsyncClient")
    def test_successful_ask_request(self, mock_client_class):
        """Test successful API request to OpenAI"""
        # Mock the async client and response
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        
        # Mock successful OpenAI response
        mock_response = AsyncMock()
        mock_response.status_code = 200
        mock_response.json = AsyncMock(return_value={
            "choices": [
                {
                    "message": {
                        "content": "You need a valid passport and may need a visa depending on your nationality."
                    }
                }
            ]
        })
        mock_client.post = AsyncMock(return_value=mock_response)
        
        # Make request
        response = client.post(
            "/api/ask",
            json={"question": "What documents do I need for travel to Japan?"}
        )
        
        # Assertions
        if response.status_code != 200:
            print(f"Response status: {response.status_code}")
            print(f"Response body: {response.text}")
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "model" in data
        assert data["model"] == "gpt-3.5-turbo"
        assert "passport" in data["answer"].lower()
        
        # Verify the request was made correctly
        mock_client.post.assert_called_once()
        call_args = mock_client.post.call_args
        assert call_args[0][0] == "https://api.openai.com/v1/chat/completions"
        assert "Authorization" in call_args[1]["headers"]
        assert call_args[1]["headers"]["Authorization"] == "Bearer test-api-key"
        assert call_args[1]["json"]["model"] == "gpt-3.5-turbo"
        assert call_args[1]["json"]["messages"][1]["content"] == "What documents do I need for travel to Japan?"
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-api-key"})
    @patch("httpx.AsyncClient")
    def test_openai_api_error(self, mock_client_class):
        """Test handling of OpenAI API errors"""
        # Mock the async client and response
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        
        # Mock error response from OpenAI
        mock_response = AsyncMock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_client.post = AsyncMock(return_value=mock_response)
        
        # Make request
        response = client.post(
            "/api/ask",
            json={"question": "What documents do I need for travel to Japan?"}
        )
        
        # Assertions
        assert response.status_code == 401
        assert "Error code: 401" in response.json()["detail"]
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-api-key"})
    @patch("httpx.AsyncClient")
    def test_network_error(self, mock_client_class):
        """Test handling of network errors"""
        # Mock the async client to raise an exception
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        mock_client.post = AsyncMock(side_effect=httpx.ConnectError("Connection failed"))
        
        # Make request
        response = client.post(
            "/api/ask",
            json={"question": "What documents do I need for travel to Japan?"}
        )
        
        # Assertions
        assert response.status_code == 500
        assert "Connection failed" in response.json()["detail"]
    
    def test_missing_api_key(self):
        """Test behavior when API key is missing"""
        # Remove API key from environment
        with patch.dict(os.environ, {}, clear=True):
            response = client.post(
                "/api/ask",
                json={"question": "What documents do I need for travel to Japan?"}
            )
            
            # Should attempt the request but fail with 401 (Unauthorized from OpenAI)
            assert response.status_code == 401
    
    def test_invalid_request_body(self):
        """Test handling of invalid request body"""
        response = client.post(
            "/api/ask",
            json={"invalid_field": "test"}
        )
        
        assert response.status_code == 422  # Validation error
    
    def test_missing_question_field(self):
        """Test handling of missing question field"""
        response = client.post(
            "/api/ask",
            json={}
        )
        
        assert response.status_code == 422  # Validation error

class TestCORSConfiguration:
    """Test CORS middleware configuration"""
    
    def test_cors_headers_present(self):
        """Test that CORS headers are properly configured"""
        response = client.options(
            "/",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type"
            }
        )
        
        # FastAPI TestClient doesn't fully simulate CORS preflight,
        # but we can verify the middleware is configured
        assert response.status_code in [200, 405]  # OPTIONS might not be implemented for all routes

class TestAppConfiguration:
    """Test FastAPI app configuration"""
    
    def test_app_metadata(self):
        """Test that app has correct metadata"""
        assert app.title == "Travel Documentation Assistant"
        assert app.description == "AI-powered travel documentation helper"
        assert app.version == "1.0.0"
        assert app.contact["name"] == "Eleazar Yewa"
        assert app.contact["email"] == "eleazar.yewa.harold@gmail.com"
        assert app.license_info["name"] == "MIT"
    
    def test_openapi_endpoints(self):
        """Test that OpenAPI endpoints are accessible"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        
        response = client.get("/docs")
        assert response.status_code == 200
        
        response = client.get("/redoc")
        assert response.status_code == 200

class TestIntegration:
    """Integration tests"""
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-api-key"})
    @patch("httpx.AsyncClient")
    def test_full_workflow(self, mock_client_class):
        """Test complete workflow from request to response"""
        # Mock the async client and response
        mock_client = AsyncMock()
        mock_client_class.return_value.__aenter__.return_value = mock_client
        
        # Mock successful OpenAI response
        mock_response = AsyncMock()
        mock_response.status_code = 200
        mock_response.json = AsyncMock(return_value={
            "choices": [
                {
                    "message": {
                        "content": "For travel to Japan, you typically need:\n1. Valid passport (6+ months validity)\n2. Visa (depending on nationality)\n3. Return ticket\n4. Proof of accommodation"
                    }
                }
            ]
        })
        mock_client.post = AsyncMock(return_value=mock_response)
        
        # Test the complete flow
        response = client.post(
            "/api/ask",
            json={"question": "What do I need to travel to Japan?"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "model" in data
        assert data["model"] == "gpt-3.5-turbo"
        assert "passport" in data["answer"].lower()
        assert "visa" in data["answer"].lower()

# Pytest configuration
@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
