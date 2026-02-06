import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { ChakraProvider, defaultSystem } from '@chakra-ui/react'
import App from './App'

function renderWithProviders(ui: React.ReactElement) {
  return render(<ChakraProvider value={defaultSystem}>{ui}</ChakraProvider>)
}

describe('App', () => {
  beforeEach(() => {
    vi.spyOn(global, 'fetch').mockResolvedValue({
      json: () => Promise.resolve({ message: 'Welcome to Cat in Box.' }),
    } as Response)
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('displays the welcome message', async () => {
    renderWithProviders(<App />)
    await waitFor(() => {
      expect(screen.getByText(/Welcome to Cat in Box/)).toBeInTheDocument()
    })
  })

  it('sends command on enter and displays response', async () => {
    const user = userEvent.setup()
    vi.spyOn(global, 'fetch')
      .mockResolvedValueOnce({
        json: () => Promise.resolve({ message: 'Welcome' }),
      } as Response)
      .mockResolvedValueOnce({
        json: () => Promise.resolve({ response: 'You said: hello' }),
      } as Response)

    renderWithProviders(<App />)

    const input = screen.getByPlaceholderText(/enter command/i)
    await user.type(input, 'hello{Enter}')

    await waitFor(() => {
      expect(screen.getByText(/> hello/)).toBeInTheDocument()
      expect(screen.getByText(/You said: hello/)).toBeInTheDocument()
    })
  })
})
