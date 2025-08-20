
import { useState } from 'react';
import './App.css';

function App() {
  const [todos, setTodos] = useState<string[]>([]);
  const [input, setInput] = useState('');

  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, input.trim()]);
      setInput('');
    }
  };

  const removeTodo = (idx: number) => {
    setTodos(todos.filter((_, i) => i !== idx));
  };

  return (
    <div className="app-container">
      <h1>Todo App</h1>
      <div className="input-section">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Add a new todo"
        />
        <button onClick={addTodo}>Add</button>
      </div>
      <ul className="todo-list">
        {todos.map((todo, idx) => (
          <li key={idx}>
            {todo}
            <button className="remove-btn" onClick={() => removeTodo(idx)}>
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
