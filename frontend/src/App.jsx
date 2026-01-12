import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
import TaskList from './components/TaskList'
import TaskForm from './components/TaskForm'

function App() {
  const [tasks, setTasks] = useState([])

  const fetchTasks = () => {
    axios.get('http://localhost:8000/tasks')
      .then(response => setTasks(response.data))
  }

  useEffect(() => {
    fetchTasks()
  }, [])

  return (
    <div>
      <h1>Productivity AI</h1>
      <TaskForm onTaskCreated={fetchTasks}/>
      <TaskList tasks={tasks} onTaskCompleted={fetchTasks}/>
    </div>
  )
}

export default App
