#!/usr/bin/env python3
"""
Start script for the Travel Documentation Assistant API
"""
import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Starting Travel Documentation Assistant API...")
    print("📚 API Documentation will be available at: http://localhost:8000/docs")
    print("🔍 Health check available at: http://localhost:8000/health")
    print("🌐 CORS enabled for: http://localhost:3000")
    print("=" * 60)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )
