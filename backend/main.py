import json
import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# from openai import OpenAI
from pydantic import BaseModel, field_validator

load_dotenv()

app = FastAPI(
    title="Travel Documentation Assistant",
    description="AI-powered travel documentation helper",
    version="1.0.0",
    contact={
        "name": "Eleazar Yewa",
        "email": "eleazar.yewa.harold@gmail.com"
    },
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    terms_of_service="https://www.google.com/policies/terms/",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str
    
    @field_validator('question')
    @classmethod
    def validate_question(cls, v):
        if not v or not v.strip():
            raise ValueError("Question cannot be empty")
        return v.strip()

@app.post("/api/ask")
async def ask_question(request: QueryRequest):
    try:
        # Use OpenAI's GPT-3.5-turbo model (free tier available)
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "You are a helpful travel assistant. Provide accurate, concise information about travel documentation requirements. Format your response with clear sections and bullet points where appropriate."},
                        {"role": "user", "content": request.question}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 500
                }
            )
            
            if response.status_code != 200:
                error_detail = f"Error code: {response.status_code} - {response.text}"
                raise HTTPException(status_code=response.status_code, detail=error_detail)
                
            data = await response.json()
            
            return {
                "answer": data["choices"][0]["message"]["content"],
                "model": "gpt-3.5-turbo"
            }
    except HTTPException:
        # Re-raise HTTPExceptions as-is
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Q&A API Server is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
    