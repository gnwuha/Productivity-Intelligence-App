import './App.css'
import TaskList from './components/TaskList'
import TaskForm from './components/TaskForm'

function App() {
  return (
    <div>
      <h1>Productivity AI</h1>
      <TaskList/>
      <TaskForm/>
      <p>Welcome to your productivity app!</p>
    </div>
  )
}

export default App
