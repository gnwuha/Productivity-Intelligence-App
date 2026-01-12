import { useState } from 'react'
import axios from 'axios'

function TaskForm({ onTaskCreated }) {
    const [title, setTitle] = useState('')
    const [category, setCategory] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()

        axios.post('http://localhost:8000/tasks', null, {
            params: {title, category}
        })
        .then(() => {
            setTitle('')
            setCategory('')
            onTaskCreated()
            alert('Task created!')
        })
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>Add Task</h2>
            <input
            type="text"
            placeholder='Task Title'
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            />

            <input
                type="text"
                placeholder="Category"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
            />
            <button type="submit">Add Task</button>
        </form>
    )
}

export default TaskForm