import { useState, useEffect } from 'react'
import axios from 'axios'

function TaskList() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/tasks')
      .then(response => {
        setTasks(response.data)
      })
  }, [])

  return (
    <div>
      <h2>My Tasks</h2>
      {tasks.map(task => (
        <div key={task.id}>
          <h3>{task.title}</h3>
          <p>Status: {task.status}</p>
        </div>
      ))}
    </div>
  )
}

export default TaskList