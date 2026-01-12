import { useState, useEffect } from 'react'
import axios from 'axios'

function TaskList({ tasks, onTaskCompleted }) {
  const handleComplete = (taskId) => {
    axios.put("http://localhost:8000/tasks/${taskID}/complete")
      .then(() => {
        onTaskCompleted()
      })
  }
  return (
    <div>
      <h2>My Tasks</h2>
      {tasks.map(task => (
        <div key={task.id}>
          <h3>{task.title}</h3>
          <p>Status: {task.status}</p>
          {task.status !== 'Completed' && (
            <button onClick={() => handleComplete(task.id)}>Complete</button>
          )}
        </div>
      ))}
    </div>
  )
}

export default TaskList