import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import words from './data/words.json';
import { Display } from './components/displayComponent';

function App() {
  const [puzzle, setPuzzle] = useState(
    Math.floor(Math.random() * words.length)
  );
  const [guessedLetters, setGuessedLetters] = useState([]);
  // console.log(words);
  // console.log(Math.floor(1 * 26));
  // console.log(words[25]);

  // console.log(puzzle);

  return (
    <div className="App">
      <Display puzzle={puzzle} />
    </div>
  );
}

export default App;
