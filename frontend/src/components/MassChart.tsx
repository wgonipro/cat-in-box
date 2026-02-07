import { Box, Text } from '@chakra-ui/react'
import { LineChart, Line, XAxis, YAxis, ResponsiveContainer, ReferenceLine } from 'recharts'

export interface FeederEvent {
  time: number
  action: 'open' | 'close'
}

interface MassChartProps {
  feederEvents?: FeederEvent[]
}

export function MassChart({ feederEvents = [] }: MassChartProps) {
  // Baseline data to establish chart coordinate system
  const data = [
    { time: 0, value: 0 },
    { time: 10, value: 0 },
  ]

  return (
    <Box
      bg="black"
      border="1px solid"
      borderColor="green.700"
      p={4}
      h="200px"
    >
      <Text color="green.400" mb={2}>Simulation Timeline (hours)</Text>
      <ResponsiveContainer width="100%" height="80%">
        <LineChart data={data}>
          <XAxis
            dataKey="time"
            domain={[0, 10]}
            ticks={[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
            stroke="#2F855A"
            tick={{ fill: '#2F855A' }}
            type="number"
          />
          <YAxis
            domain={[0, 100]}
            stroke="#2F855A"
            tick={{ fill: '#2F855A' }}
          />
          <Line
            type="monotone"
            dataKey="value"
            stroke="transparent"
            dot={false}
          />
          {feederEvents.map((event, i) => (
            <ReferenceLine
              key={i}
              x={event.time}
              stroke={event.action === 'open' ? '#48BB78' : '#E53E3E'}
              strokeWidth={2}
              strokeDasharray="4 2"
              label={{
                value: `${event.action} feeder`,
                fill: event.action === 'open' ? '#48BB78' : '#E53E3E',
                fontSize: 10,
                position: 'top',
              }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </Box>
  )
}
