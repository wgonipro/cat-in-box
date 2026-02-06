import { useState, useEffect, KeyboardEvent } from 'react'
import { Box, Input, Text, VStack, ScrollArea } from '@chakra-ui/react'

function App() {
  const [log, setLog] = useState<string[]>([])
  const [input, setInput] = useState('')

  useEffect(() => {
    fetch('/api/')
      .then((res) => res.json())
      .then((data) => setLog([data.message]))
  }, [])

  const handleKeyDown = async (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && input.trim()) {
      const userInput = input.trim()
      setInput('')
      setLog((prev) => [...prev, `> ${userInput}`])

      const res = await fetch('/api/command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: userInput }),
      })
      const data = await res.json()
      setLog((prev) => [...prev, data.response])
    }
  }

  return (
    <Box bg="black" minH="100vh" p={4} fontFamily="mono">
      <VStack align="stretch" maxW="800px" mx="auto" gap={4}>
        <ScrollArea.Root
          h="400px"
          bg="black"
          border="1px solid"
          borderColor="green.700"
        >
          <ScrollArea.Viewport p={4} color="green.400">
            {log.map((line, i) => (
              <Text key={i} whiteSpace="pre-wrap">{line}</Text>
            ))}
          </ScrollArea.Viewport>
          <ScrollArea.Scrollbar orientation="vertical">
              <ScrollArea.Thumb bg="green.400" />
            </ScrollArea.Scrollbar>
        </ScrollArea.Root>
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter command..."
          bg="black"
          color="green.400"
          border="1px solid"
          borderColor="green.700"
          _placeholder={{ color: 'green.700' }}
          _focus={{ borderColor: 'green.400', boxShadow: 'none' }}
        />
      </VStack>
    </Box>
  )
}

export default App
