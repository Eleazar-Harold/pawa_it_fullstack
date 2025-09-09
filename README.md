# Travel Documentation Assistant

A modern, full-stack web application that provides AI-powered answers to travel documentation questions. Built with FastAPI backend and Next.js frontend, featuring comprehensive testing, responsive design, and robust error handling.

## 🚀 Features

### Backend Features
- **🤖 AI-Powered Assistance** - OpenAI GPT-3.5-turbo integration for intelligent responses
- **🌐 RESTful API** - FastAPI with auto-generated documentation
- **🔒 CORS Support** - Seamless frontend integration
- **✅ Comprehensive Testing** - Full test coverage with pytest
- **📚 Auto Documentation** - Swagger UI and ReDoc endpoints
- **🚀 Production Ready** - Optimized for deployment

### Frontend Features
- **📱 Responsive Design** - Beautiful, mobile-first UI with Tailwind CSS
- **⚡ Fast Performance** - Optimized Next.js with static generation
- **🧪 Comprehensive Testing** - Jest and React Testing Library
- **🔒 Error Handling** - Robust error handling with user feedback
- **♿ Accessibility** - Built with accessibility best practices
- **🌐 Real-time Communication** - Seamless API integration

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.104.1
- **Language**: Python 3.12+
- **AI Integration**: OpenAI GPT-3.5-turbo
- **Testing**: pytest + pytest-asyncio
- **Server**: Uvicorn
- **Documentation**: Swagger UI + ReDoc

### Frontend
- **Framework**: Next.js 14.2.32
- **UI Library**: React 18.2.0
- **Styling**: Tailwind CSS 3.3.5
- **Testing**: Jest + React Testing Library
- **Build Tool**: Next.js built-in bundler
- **Package Manager**: npm

## 📁 Project Structure

```
fullstackapp/
├── backend/                    # FastAPI backend application
│   ├── main.py                # Main FastAPI application
│   ├── test_main.py           # Comprehensive test suite
│   ├── start_server.py        # Development server script
│   ├── run_tests.py           # Test runner script
│   ├── requirements.txt       # Python dependencies
│   ├── pyproject.toml         # Project configuration
│   ├── pytest.ini            # Pytest configuration
│   └── README.md             # Backend documentation
├── frontend/                   # Next.js frontend application
│   ├── components/
│   │   └── TravelAssistant.js # Main application component
│   ├── pages/
│   │   └── index.js          # Home page
│   ├── __tests__/            # Test suites
│   ├── jest.config.js        # Jest configuration
│   ├── jest.setup.js         # Test setup and mocks
│   ├── run_tests.js          # Test runner script
│   ├── TESTING.md            # Detailed testing documentation
│   ├── package.json          # Node.js dependencies
│   ├── tailwind.config.js    # Tailwind CSS configuration
│   └── README.md             # Frontend documentation
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18+ (for frontend)
- **Python** 3.12+ (for backend)
- **OpenAI API Key** (for AI functionality)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fullstackapp
```

### 2. Backend Setup

#### Navigate to Backend Directory
```bash
cd backend
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables
```bash
# Create .env file
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

#### Run the Backend Server
```bash
# Option 1: Using the start script
python start_server.py

# Option 2: Using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Backend will be available at:**
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### 3. Frontend Setup

#### Navigate to Frontend Directory (New Terminal)
```bash
cd frontend
```

#### Install Dependencies
```bash
npm install
```

#### Start Development Server
```bash
npm run dev
```

**Frontend will be available at:** http://localhost:3000

### 4. Getting Your OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up for an account
3. Generate an API key from your dashboard
4. Add the API key to your backend `.env` file

## 📜 Available Scripts

### Backend Scripts
```bash
# Development
python start_server.py          # Start development server
uvicorn main:app --reload       # Start with uvicorn directly

# Testing
python -m pytest test_main.py -v           # Run all tests
python -m pytest test_main.py --cov=main   # Run with coverage
python run_tests.py                        # Use test runner script

# Production
uvicorn main:app --host 0.0.0.0 --port 8000  # Production server
```

### Frontend Scripts
```bash
# Development
npm run dev          # Start development server with hot reload
npm run build        # Build production-ready application
npm run start        # Start production server
npm run lint         # Run ESLint for code quality

# Testing
npm test             # Run all tests
npm run test:watch   # Run tests in watch mode
npm run test:coverage # Run tests with coverage report
node run_tests.js    # Use custom test runner
```

## 🧪 Testing

### Backend Testing
The backend includes comprehensive testing with **25+ passing tests**:

```bash
# Run all backend tests
cd backend
python -m pytest test_main.py -v

# Run specific test categories
python -m pytest test_main.py::TestQueryRequest -v
python -m pytest test_main.py::TestAskEndpoint -v
```

**Test Categories:**
- **Model Validation** - QueryRequest validation tests
- **API Endpoints** - All HTTP endpoint tests
- **Error Handling** - Various error scenario tests
- **CORS Configuration** - CORS middleware tests
- **Integration Tests** - End-to-end workflow tests

### Frontend Testing
The frontend includes comprehensive testing with **7+ passing tests**:

```bash
# Run all frontend tests
cd frontend
npm test

# Run specific test files
npm test TravelAssistant.simple.test.js
```

**Test Categories:**
- **Component Rendering** - UI elements render correctly
- **User Interactions** - Input changes, form submissions, button clicks
- **API Integration** - Successful requests, error handling, network failures
- **State Management** - Loading states, error states, response display
- **Error Handling** - Validation errors, API errors, network errors
- **Response Management** - Display responses, clear functionality

## 🌐 API Documentation

### Backend API Endpoints

#### Core Endpoints
- `GET /` - Root endpoint with server status
- `GET /health` - Health check endpoint
- `POST /api/ask` - Ask travel documentation questions

#### Documentation Endpoints
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)
- `GET /openapi.json` - OpenAPI schema

### API Usage Examples

#### Ask a Travel Question
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

#### Health Check
```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

## 🔧 Configuration

### Backend Configuration

#### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-3.5-turbo | Yes |

#### CORS Settings
- **Origin**: `http://localhost:3000` (for frontend development)
- **Methods**: All methods (`*`)
- **Headers**: All headers (`*`)
- **Credentials**: Enabled

### Frontend Configuration

#### Environment Variables
Create a `.env.local` file:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

#### Tailwind CSS
Configuration in `tailwind.config.js`:
```javascript
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## 🚀 Deployment

### Backend Deployment

#### Production Considerations
1. **Environment Variables**: Set `OPENAI_API_KEY` in production
2. **CORS**: Update allowed origins for production domains
3. **Security**: Consider adding authentication/rate limiting
4. **Monitoring**: Add logging and health checks
5. **Scaling**: Use a production ASGI server like Gunicorn

#### Docker Deployment
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend Deployment

#### Production Build
```bash
cd frontend
npm run build
```

#### Deployment Platforms
- **Vercel** (Recommended for Next.js)
- **Netlify**
- **AWS Amplify**
- **Docker** (with custom Dockerfile)

## 🎯 Usage Examples

### Example Questions
- "What documents do I need to travel from Kenya to Ireland?"
- "What's the visa requirement for US citizens visiting Brazil?"
- "Do I need vaccinations to travel to Thailand?"
- "What are the passport requirements for traveling to Japan?"
- "How long can I stay in the EU with a US passport?"

### User Workflow
1. Open your browser and navigate to http://localhost:3000
2. Type your travel documentation question in the input field
3. Click "Ask Question" to get an AI-generated response
4. View the formatted response with model information
5. Clear the response to ask another question

## 🐛 Troubleshooting

### Common Issues

#### Backend Issues
1. **API Key Not Working**
   - Verify `OPENAI_API_KEY` is set in `.env` file
   - Check API key has sufficient credits
   - Ensure API key is valid and active

2. **CORS Errors**
   - Verify CORS is configured for frontend URL
   - Check that frontend is running on correct port
   - Ensure backend allows the frontend origin

3. **Tests Failing**
   - Run `pip install -r requirements.txt` to ensure dependencies
   - Check Python version compatibility
   - Verify test environment setup

#### Frontend Issues
1. **API Connection Failed**
   - Ensure backend is running on `http://localhost:8000`
   - Check CORS configuration
   - Verify API endpoint availability

2. **Tests Failing**
   - Run `npm install` to ensure dependencies are installed
   - Check Jest configuration
   - Verify test environment setup

3. **Build Errors**
   - Clear `.next` directory: `rm -rf .next`
   - Reinstall dependencies: `rm -rf node_modules && npm install`
   - Check for TypeScript errors (if using TS)

### Debug Mode
```bash
# Backend debug
cd backend
uvicorn main:app --reload --log-level debug

# Frontend debug
cd frontend
DEBUG=* npm run dev
```

## 📚 Documentation References

### Internal Documentation
- **[Backend README](./backend/README.md)** - Detailed backend documentation
- **[Frontend README](./frontend/README.md)** - Detailed frontend documentation
- **[Frontend Testing Guide](./frontend/TESTING.md)** - Comprehensive testing documentation

### External Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contributing

### Development Guidelines
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests for both backend and frontend
6. Commit changes: `git commit -m 'Add feature'`
7. Push to branch: `git push origin feature-name`
8. Submit a pull request

### Code Quality Standards
- **Backend**: All functions must be tested, use type hints, follow Python best practices
- **Frontend**: Write tests for new features, follow React best practices, ensure accessibility
- **Documentation**: Update relevant README files and add inline comments
- **Testing**: Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the internal documentation in `backend/README.md` and `frontend/README.md`
- Review the troubleshooting section above
- Create an issue in the project repository
- Check the test suites for usage examples

---

**Built with ❤️ using FastAPI, Next.js, React, and Tailwind CSS**