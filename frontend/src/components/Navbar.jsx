import { Link } from 'react-router-dom'

function Navbar() {
    return (
        <nav>
            <h1>Productivity AI</h1>
            <div>
                <Link to="/">Home</Link>
                <Link to="/tasks">Tasks</Link>
                <Link to="/wellness">Wellness Checks</Link>
                <Link to="/insights">Insights</Link>
            </div>
        </nav>
    )
}

export default Navbar