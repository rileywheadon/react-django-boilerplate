import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Fetch data from Django API
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/hello/')
        setMessage(response.data.message)
      } catch (error) {
        console.error('Error fetching data:', error)
        setMessage('Error connecting to Django backend')
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>React + Django Boilerplate</h1>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <p>{message}</p>
        )}
        <div className="card">
          <button onClick={() => setMessage('Hello from React!')}>
            Update Message
          </button>
        </div>
      </header>
    </div>
  )
}

export default App