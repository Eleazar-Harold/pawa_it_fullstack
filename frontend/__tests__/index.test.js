import { render, screen } from '@testing-library/react';
import Home from '../pages/index';

// Mock the TravelAssistant component
jest.mock('../components/TravelAssistant', () => {
  return function MockTravelAssistant() {
    return <div data-testid="travel-assistant">Travel Assistant Component</div>;
  };
});

describe('Home Page', () => {
  test('renders the main page with correct title', () => {
    render(<Home />);
    
    // Check if the page title is set correctly
    expect(document.title).toBe('Travel Documentation Assistant');
  });

  test('renders the TravelAssistant component', () => {
    render(<Home />);
    
    expect(screen.getByTestId('travel-assistant')).toBeInTheDocument();
    expect(screen.getByText('Travel Assistant Component')).toBeInTheDocument();
  });

  test('includes proper meta tags', () => {
    render(<Home />);
    
    // Check for meta description
    const metaDescription = document.querySelector('meta[name="description"]');
    expect(metaDescription).toBeInTheDocument();
    expect(metaDescription).toHaveAttribute('content', 'AI-powered travel documentation helper');
    
    // Check for viewport meta tag
    const metaViewport = document.querySelector('meta[name="viewport"]');
    expect(metaViewport).toBeInTheDocument();
    expect(metaViewport).toHaveAttribute('content', 'width=device-width, initial-scale=1');
  });
});
