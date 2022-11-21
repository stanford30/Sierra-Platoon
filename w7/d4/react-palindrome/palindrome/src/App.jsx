import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import Palindrome from './components/palindrome';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <Palindrome />
    </div>
  );
}

export default App;
