import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0) 
  return (
    <div>
      <h1>Productivity AI</h1>
      <p>Welcome to your productivity app!</p>
    </div>
  )
}

export default App
