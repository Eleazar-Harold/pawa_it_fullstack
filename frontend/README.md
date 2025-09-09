# Travel Documentation Assistant - Frontend

A modern, responsive Next.js frontend application for the Travel Documentation Assistant. This application provides an intuitive interface for users to ask questions about travel documentation requirements and receive AI-powered responses.

## 🚀 Features

- **🤖 AI-Powered Assistance** - Get intelligent responses about travel documentation requirements
- **📱 Responsive Design** - Beautiful, mobile-first UI built with Tailwind CSS
- **⚡ Fast Performance** - Optimized Next.js application with static generation
- **🧪 Comprehensive Testing** - Full test coverage with Jest and React Testing Library
- **🔒 Error Handling** - Robust error handling with user-friendly feedback
- **♿ Accessibility** - Built with accessibility best practices
- **🌐 CORS Support** - Seamless integration with backend API

## 🛠️ Tech Stack

- **Framework**: Next.js 14.2.32
- **UI Library**: React 18.2.0
- **Styling**: Tailwind CSS 3.3.5
- **Testing**: Jest + React Testing Library
- **Build Tool**: Next.js built-in bundler
- **Package Manager**: npm

## 📁 Project Structure

```
frontend/
├── components/
│   └── TravelAssistant.js      # Main application component
├── pages/
│   └── index.js                # Home page
├── __tests__/
│   ├── TravelAssistant.simple.test.js  # Core functionality tests
│   ├── TravelAssistant.test.js         # Comprehensive unit tests
│   ├── index.test.js                   # Page component tests
│   └── integration.test.js             # Integration tests
├── .next/                      # Next.js build output
├── node_modules/               # Dependencies
├── jest.config.js              # Jest configuration
├── jest.setup.js               # Test setup and mocks
├── run_tests.js                # Test runner script
├── TESTING.md                  # Detailed testing documentation
├── package.json                # Dependencies and scripts
├── tailwind.config.js          # Tailwind CSS configuration
├── postcss.config.js           # PostCSS configuration
└── .gitignore                  # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running on `http://localhost:8000`

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fullstackapp/frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 📜 Available Scripts

### Development
```bash
npm run dev          # Start development server with hot reload
npm run build        # Build production-ready application
npm run start        # Start production server
npm run lint         # Run ESLint for code quality
```

### Testing
```bash
npm test             # Run all tests
npm run test:watch   # Run tests in watch mode
npm run test:coverage # Run tests with coverage report
node run_tests.js    # Use custom test runner
```

### Build & Deploy
```bash
npm run build        # Create optimized production build
npm run start        # Start production server
```

## 🧪 Testing

The application includes comprehensive testing with **7 passing tests** covering:

### Test Categories
- **Component Rendering** - UI elements render correctly
- **User Interactions** - Input changes, form submissions, button clicks  
- **API Integration** - Successful requests, error handling, network failures
- **State Management** - Loading states, error states, response display
- **Error Handling** - Validation errors, API errors, network errors
- **Response Management** - Display responses, clear functionality

### Running Tests
```bash
# Run all tests
npm test

# Run specific test file
npm test TravelAssistant.simple.test.js

# Run tests with coverage
npm run test:coverage

# Run tests in watch mode
npm run test:watch
```

### Test Coverage
- **Total Tests**: 7+ tests
- **Coverage Target**: 80%
- **Test Categories**: 3 (Unit, Integration, Page)
- **Mocked Dependencies**: Next.js router, Head component, fetch API

For detailed testing information, see [TESTING.md](./TESTING.md).

## 🎨 UI Components

### TravelAssistant Component

The main component that handles:
- **Input Management** - Text input with validation
- **API Communication** - Fetch requests to backend
- **State Management** - Loading, error, and response states
- **User Feedback** - Error messages and success responses
- **Response Display** - Formatted AI responses with clear functionality

### Key Features
- **Real-time Validation** - Input validation with immediate feedback
- **Loading States** - Visual feedback during API calls
- **Error Handling** - User-friendly error messages
- **Responsive Design** - Works on all device sizes
- **Accessibility** - ARIA labels and keyboard navigation

## 🔧 Configuration

### Environment Variables
Create a `.env.local` file for environment-specific configuration:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Tailwind CSS
The application uses Tailwind CSS for styling. Configuration is in `tailwind.config.js`:
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

### Jest Configuration
Testing is configured in `jest.config.js` with:
- Next.js integration
- JSDOM environment
- Custom matchers from `@testing-library/jest-dom`
- Coverage thresholds

## 🌐 API Integration

The frontend communicates with the backend API:

### Endpoints
- `POST /api/ask` - Submit travel documentation questions

### Request Format
```javascript
{
  "question": "What documents do I need for Japan?"
}
```

### Response Format
```javascript
{
  "answer": "You need a valid passport and visa for Japan.",
  "model": "gpt-3.5-turbo"
}
```

### Error Handling
- **Network Errors** - Connection failures
- **API Errors** - Server errors (4xx, 5xx)
- **Validation Errors** - Invalid input
- **Response Errors** - Malformed responses

## 🚀 Deployment

### Production Build
```bash
npm run build
```

### Static Export (Optional)
```bash
npm run build
npm run export
```

### Deployment Platforms
- **Vercel** (Recommended for Next.js)
- **Netlify**
- **AWS Amplify**
- **Docker** (with custom Dockerfile)

### Environment Setup
Ensure the backend API is accessible at the configured URL in production.

## 🔍 Development

### Code Structure
- **Components** - Reusable UI components
- **Pages** - Next.js page components
- **Tests** - Comprehensive test suites
- **Styles** - Tailwind CSS classes
- **Configuration** - Build and test configs

### Best Practices
- **Component Composition** - Small, focused components
- **Error Boundaries** - Graceful error handling
- **Accessibility** - ARIA labels and semantic HTML
- **Performance** - Optimized images and code splitting
- **Testing** - Comprehensive test coverage

### Code Quality
- **ESLint** - Code linting and formatting
- **Prettier** - Code formatting (if configured)
- **TypeScript** - Type safety (optional upgrade)
- **Husky** - Git hooks (optional)

## 🐛 Troubleshooting

### Common Issues

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

4. **Styling Issues**
   - Verify Tailwind CSS is properly configured
   - Check PostCSS configuration
   - Ensure CSS classes are not purged

### Debug Mode
```bash
# Enable debug logging
DEBUG=* npm run dev

# Run tests with verbose output
npm test -- --verbose
```

## 📚 Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Jest Documentation](https://jestjs.io/docs/getting-started)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `npm test`
6. Commit changes: `git commit -m 'Add feature'`
7. Push to branch: `git push origin feature-name`
8. Submit a pull request

### Development Guidelines
- Write tests for new features
- Follow existing code style
- Update documentation as needed
- Ensure all tests pass
- Test on multiple devices/browsers

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the [TESTING.md](./TESTING.md) for testing-related questions
- Review the troubleshooting section above

---

**Built with ❤️ using Next.js, React, and Tailwind CSS**
