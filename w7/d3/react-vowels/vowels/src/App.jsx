import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import DisplayWord from './displayWord';

function App() {
  const [word, setWord] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    setSubmitted(false);
    setWord(e.target.value);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };
  const display = () => {
    if (submitted) {
      return <DisplayWord word={word} />;
    }
  };
  return (
    <div className="App">
      <form>
        <input onChange={handleChange} />
        <button onClick={handleSubmit}>Submit</button>
      </form>
      {display()}
    </div>
  );
}

export default App;
