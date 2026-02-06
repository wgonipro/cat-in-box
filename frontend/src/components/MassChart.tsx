import { useState, useEffect, useRef } from 'react'
import { Box, Text } from '@chakra-ui/react'
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer } from 'recharts'

interface DataPoint {
  time: number
  mass: number
}

export function MassChart() {
  const [data, setData] = useState<DataPoint[]>([])
  const startTime = useRef(Date.now())

  useEffect(() => {
    const ws = new WebSocket(`ws://${window.location.host}/ws/sensors`)

    ws.onmessage = (event) => {
      const reading = JSON.parse(event.data)
      const elapsed = Math.floor((Date.now() - startTime.current) / 1000)

      setData((prev) => {
        const next = [...prev, { time: elapsed, mass: reading.mass }]
        // Keep last 60 seconds of data
        return next.slice(-60)
      })
    }

    ws.onerror = (error) => {
      console.error('WebSocket error:', error)
    }

    return () => ws.close()
  }, [])

  return (
    <Box
      bg="black"
      border="1px solid"
      borderColor="green.700"
      p={4}
      h="200px"
    >
      <Text color="green.400" mb={2}>Mass Scale (g)</Text>
      <ResponsiveContainer width="100%" height="80%">
        <LineChart data={data}>
          <XAxis
            dataKey="time"
            stroke="#2F855A"
            tick={{ fill: '#2F855A' }}
          />
          <YAxis
            domain={[0, 100]}
            stroke="#2F855A"
            tick={{ fill: '#2F855A' }}
          />
          <Line
            type="monotone"
            dataKey="mass"
            stroke="#48BB78"
            dot={false}
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    </Box>
  )
}
