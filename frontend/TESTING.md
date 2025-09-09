# Frontend Testing Guide

This document provides comprehensive information about testing the Travel Documentation Assistant frontend application.

## 🧪 Test Setup

The frontend uses **Jest** and **React Testing Library** for comprehensive testing.

### Dependencies

- `@testing-library/react` - React component testing utilities
- `@testing-library/jest-dom` - Custom Jest matchers for DOM elements
- `@testing-library/user-event` - User interaction simulation
- `jest` - JavaScript testing framework
- `jest-environment-jsdom` - DOM environment for Jest

## 📁 Test Structure

```
frontend/
├── __tests__/
│   ├── TravelAssistant.test.js    # Component unit tests
│   ├── index.test.js              # Page component tests
│   └── integration.test.js        # Integration tests
├── components/
│   └── TravelAssistant.js         # Main component
├── pages/
│   └── index.js                   # Main page
├── jest.config.js                 # Jest configuration
├── jest.setup.js                  # Jest setup file
└── run_tests.js                   # Test runner script
```

## 🚀 Running Tests

### Basic Commands

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test TravelAssistant.test.js

# Run tests matching a pattern
npm test -- --testNamePattern="User Interactions"
```

### Using the Test Runner Script

```bash
# Run all tests
node run_tests.js

# Run tests in watch mode
node run_tests.js watch

# Run tests with coverage
node run_tests.js coverage

# Run tests for CI
node run_tests.js ci
```

## 📋 Test Categories

### 1. Component Unit Tests (`TravelAssistant.test.js`)

**Rendering Tests:**
- ✅ Renders main heading
- ✅ Renders input field with correct placeholder
- ✅ Renders submit button
- ✅ Does not render response container initially
- ✅ Does not render error message initially

**User Interaction Tests:**
- ✅ Updates input value when user types
- ✅ Clears error when user starts typing

**Form Submission Tests:**
- ✅ Shows error when submitting empty form
- ✅ Shows error when submitting form with only whitespace
- ✅ Successfully submits form with valid input
- ✅ Handles API error response
- ✅ Handles network error
- ✅ Handles invalid response format

**Response Display Tests:**
- ✅ Displays response correctly
- ✅ Clears response when clear button is clicked

**API Integration Tests:**
- ✅ Calls correct API endpoint with correct data
- ✅ Trims whitespace from input before sending

**Loading State Tests:**
- ✅ Shows loading state during API call

### 2. Page Component Tests (`index.test.js`)

- ✅ Renders the main page with correct title
- ✅ Renders the TravelAssistant component
- ✅ Includes proper meta tags

### 3. Integration Tests (`integration.test.js`)

**Complete User Journey:**
- ✅ Complete flow: ask question → get response → clear response
- ✅ Error handling flow: network error → retry with success

**Multiple API Calls:**
- ✅ Handles multiple sequential API calls

**Edge Cases:**
- ✅ Handles very long input
- ✅ Handles special characters in input
- ✅ Handles rapid successive clicks

## 🎯 Test Coverage

The test suite aims for **80% coverage** across:
- **Branches**: 80%
- **Functions**: 80%
- **Lines**: 80%
- **Statements**: 80%

### Coverage Reports

```bash
# Generate coverage report
npm run test:coverage

# View coverage in browser
open coverage/lcov-report/index.html
```

## 🔧 Test Configuration

### Jest Configuration (`jest.config.js`)

```javascript
const customJestConfig = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  testEnvironment: 'jsdom',
  testPathIgnorePatterns: ['<rootDir>/.next/', '<rootDir>/node_modules/'],
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/$1',
  },
  collectCoverageFrom: [
    'pages/**/*.{js,jsx}',
    'components/**/*.{js,jsx}',
    'utils/**/*.{js,jsx}',
    '!**/*.d.ts',
    '!**/node_modules/**',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
}
```

### Jest Setup (`jest.setup.js`)

- Imports `@testing-library/jest-dom` matchers
- Mocks Next.js router
- Mocks Next.js Head component
- Sets up global fetch mock
- Configures console.error handling

## 🧩 Mocking Strategy

### API Mocking

```javascript
// Mock successful response
fetch.mockResolvedValueOnce({
  ok: true,
  json: async () => ({
    answer: 'You need a valid passport and visa for Japan.',
    model: 'gpt-3.5-turbo'
  }),
});

// Mock error response
fetch.mockResolvedValueOnce({
  ok: false,
  status: 500,
});

// Mock network error
fetch.mockRejectedValueOnce(new Error('Network error'));
```

### Component Mocking

```javascript
// Mock Next.js components
jest.mock('next/head', () => {
  return function Head({ children }) {
    return <>{children}</>
  }
});
```

## 📝 Writing Tests

### Test Structure

```javascript
describe('ComponentName', () => {
  beforeEach(() => {
    // Setup before each test
  });

  afterEach(() => {
    // Cleanup after each test
  });

  describe('Feature Group', () => {
    test('should do something specific', async () => {
      // Arrange
      const user = userEvent.setup();
      render(<Component />);
      
      // Act
      await user.click(screen.getByTestId('button'));
      
      // Assert
      expect(screen.getByText('Expected Result')).toBeInTheDocument();
    });
  });
});
```

### Best Practices

1. **Use data-testid attributes** for reliable element selection
2. **Mock external dependencies** (APIs, modules)
3. **Test user interactions** with `@testing-library/user-event`
4. **Use async/await** for handling promises
5. **Clean up after tests** to avoid side effects
6. **Write descriptive test names** that explain the expected behavior
7. **Group related tests** using `describe` blocks

### Example Test

```javascript
test('successfully submits form with valid input', async () => {
  const user = userEvent.setup();
  const mockResponse = {
    answer: 'You need a valid passport and visa for Japan.',
    model: 'gpt-3.5-turbo'
  };

  fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => mockResponse,
  });

  render(<TravelAssistant />);
  
  const input = screen.getByTestId('query-input');
  const button = screen.getByTestId('submit-button');
  
  await user.type(input, 'What documents do I need for Japan?');
  await user.click(button);
  
  await waitFor(() => {
    expect(screen.getByTestId('response-container')).toBeInTheDocument();
    expect(screen.getByTestId('response-answer')).toHaveTextContent(mockResponse.answer);
  });
});
```

## 🐛 Debugging Tests

### Common Issues

1. **Async operations not completing**: Use `waitFor()` or `findBy*` queries
2. **Elements not found**: Check if elements are conditionally rendered
3. **Mock not working**: Ensure mocks are set up before the test runs
4. **State not updating**: Use `act()` wrapper for state updates

### Debug Commands

```bash
# Run tests with verbose output
npm test -- --verbose

# Run specific test with debug info
npm test -- --testNamePattern="specific test" --verbose

# Run tests and keep open for debugging
npm run test:watch
```

## 🔄 Continuous Integration

### GitHub Actions Example

```yaml
name: Frontend Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run test:coverage
      - uses: codecov/codecov-action@v1
```

## 📊 Test Metrics

- **Total Tests**: 25+ tests
- **Coverage Target**: 80%
- **Test Categories**: 3 (Unit, Integration, Page)
- **Mocked Dependencies**: Next.js router, Head component, fetch API

## 🚀 Future Improvements

1. **Visual Regression Testing** with Storybook
2. **E2E Testing** with Playwright or Cypress
3. **Performance Testing** with React Testing Library
4. **Accessibility Testing** with jest-axe
5. **Component Testing** with Storybook

## 📚 Resources

- [React Testing Library Documentation](https://testing-library.com/docs/react-testing-library/intro/)
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [Next.js Testing Guide](https://nextjs.org/docs/testing)
- [Testing Best Practices](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)
