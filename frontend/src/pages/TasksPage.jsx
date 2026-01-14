import { useState, useEffect } from 'react'
import axios from 'axios'
import TaskForm from './components/TaskForm'
import TaskList from './components/TaskList'


function TasksPage(){
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
            <h2>Task Management</h2>
            <TaskForm onTaskCreated={fetchTasks}/>
            <TaskList tasks={tasks} onTaskCompleted={fetchTasks}/>
        </div>
    )
}

export default TasksPage