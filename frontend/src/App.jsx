import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState(null)

  useEffect(() => {
    fetch('/api/')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
  }, [])

  return (
    <div className="card">
      <h1>Cat in Box</h1>
      <p>Backend says: {message ?? 'Loading...'}</p>
    </div>
  )
}

export default App
