# Travel Documentation Assistant API

A FastAPI-based backend service that provides AI-powered travel documentation assistance using OpenAI's GPT-3.5-turbo model.

## Features

- 🤖 AI-powered travel documentation assistance
- 🌐 RESTful API with FastAPI
- 📚 Auto-generated API documentation
- 🔒 CORS support for frontend integration
- ✅ Comprehensive test coverage
- 🚀 Easy deployment and development setup

## API Endpoints

### Core Endpoints

- `GET /` - Root endpoint with server status
- `GET /health` - Health check endpoint
- `POST /api/ask` - Ask travel documentation questions

### Documentation

- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)
- `GET /openapi.json` - OpenAPI schema

## Quick Start

### Prerequisites

- Python 3.12+
- OpenAI API key

### Installation

1. **Clone and navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

4. **Run the application:**
   ```bash
   python start_server.py
   ```

   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## Usage Examples

### Ask a Travel Question

```bash
curl -X POST "http://localhost:8000/api/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What documents do I need to travel to Japan?"}'
```

**Response:**
```json
{
  "answer": "For travel to Japan, you typically need:\n1. Valid passport (6+ months validity)\n2. Visa (depending on nationality)\n3. Return ticket\n4. Proof of accommodation",
  "model": "gpt-3.5-turbo"
}
```

### Health Check

```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest test_main.py -v

# Run specific test categories
python -m pytest test_main.py::TestQueryRequest -v
python -m pytest test_main.py::TestAskEndpoint -v

# Run with coverage
python -m pytest test_main.py --cov=main --cov-report=html
```

### Test Categories

- **Model Validation**: Tests for QueryRequest validation
- **API Endpoints**: Tests for all HTTP endpoints
- **Error Handling**: Tests for various error scenarios
- **CORS Configuration**: Tests for CORS middleware
- **Integration Tests**: End-to-end workflow tests

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-3.5-turbo | Yes |

### CORS Settings

The API is configured to allow requests from:
- Origin: `http://localhost:3000` (for frontend development)
- Methods: All methods (`*`)
- Headers: All headers (`*`)
- Credentials: Enabled

## API Schema

### QueryRequest Model

```python
{
  "question": "string"  # Required, non-empty travel question
}
```

### Response Model

```python
{
  "answer": "string",   # AI-generated response
  "model": "string"     # Model used (gpt-3.5-turbo)
}
```

## Error Handling

The API handles various error scenarios:

- **400 Bad Request**: Invalid request body or validation errors
- **401 Unauthorized**: Missing or invalid OpenAI API key
- **500 Internal Server Error**: Unexpected server errors or network issues

## Development

### Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── test_main.py         # Comprehensive test suite
├── start_server.py      # Development server script
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project configuration
├── pytest.ini          # Pytest configuration
└── README.md           # This file
```

### Adding New Features

1. **Add new endpoints** in `main.py`
2. **Write tests** in `test_main.py`
3. **Update documentation** in this README
4. **Run tests** to ensure everything works

### Code Quality

- All functions are properly tested
- Type hints are used throughout
- Error handling is comprehensive
- Code follows Python best practices

## Deployment

### Production Considerations

1. **Environment Variables**: Set `OPENAI_API_KEY` in production
2. **CORS**: Update allowed origins for production domains
3. **Security**: Consider adding authentication/rate limiting
4. **Monitoring**: Add logging and health checks
5. **Scaling**: Use a production ASGI server like Gunicorn

### Docker Deployment

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Check the test suite for usage examples
- Review the API documentation at `/docs`
- Open an issue in the project repository
