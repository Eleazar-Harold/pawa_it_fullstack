import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import TravelAssistant from '../components/TravelAssistant';

// Mock fetch globally
global.fetch = jest.fn();

describe('TravelAssistant - Simple Tests', () => {
  beforeEach(() => {
    fetch.mockClear();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test('renders the main heading', () => {
    render(<TravelAssistant />);
    expect(screen.getByText('Travel Documentation Assistant')).toBeInTheDocument();
  });

  test('renders input field and submit button', () => {
    render(<TravelAssistant />);
    expect(screen.getByTestId('query-input')).toBeInTheDocument();
    expect(screen.getByTestId('submit-button')).toBeInTheDocument();
  });

  test('updates input value when user types', async () => {
    const user = userEvent.setup();
    render(<TravelAssistant />);
    
    const input = screen.getByTestId('query-input');
    await user.type(input, 'What documents do I need for Japan?');
    
    expect(input).toHaveValue('What documents do I need for Japan?');
  });

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

    expect(fetch).toHaveBeenCalledWith('http://localhost:8000/api/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: 'What documents do I need for Japan?' }),
    });
  });

  test('handles API error response', async () => {
    const user = userEvent.setup();
    
    fetch.mockResolvedValueOnce({
      ok: false,
      status: 500,
    });

    render(<TravelAssistant />);
    
    const input = screen.getByTestId('query-input');
    const button = screen.getByTestId('submit-button');
    
    await user.type(input, 'What documents do I need for Japan?');
    await user.click(button);
    
    await waitFor(() => {
      expect(screen.getByTestId('error-message')).toBeInTheDocument();
    });
  });

  test('handles network error', async () => {
    const user = userEvent.setup();
    
    fetch.mockRejectedValueOnce(new Error('Network error'));

    render(<TravelAssistant />);
    
    const input = screen.getByTestId('query-input');
    const button = screen.getByTestId('submit-button');
    
    await user.type(input, 'What documents do I need for Japan?');
    await user.click(button);
    
    await waitFor(() => {
      expect(screen.getByTestId('error-message')).toBeInTheDocument();
    });
  });

  test('clears response when clear button is clicked', async () => {
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
    });

    const clearButton = screen.getByTestId('clear-button');
    await user.click(clearButton);
    
    expect(screen.queryByTestId('response-container')).not.toBeInTheDocument();
  });
});
