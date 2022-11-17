import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import DisplayWord from './displayWord';

function App() {
  const [word, setWord] = useState('');
  // const [submitted, setSubmitted] = useState(false);
  const [wordList, setWordList] = useState([]);

  const handleChange = (e) => {
    // setSubmitted(false);
    setWord(e.target.value);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    // console.log(e);

    setWordList([...wordList, word]);
    setWord('');

    // setSubmitted(true);
  };
  const displayWord = (word) => {
    return <DisplayWord word={word} />;
  };

  const displayWords = () => {
    let res = [];
    for (let x of wordList) {
      // console.log(x);

      res.push(displayWord(x));
    }
    return res.map((el) => el);
  };
  return (
    <div className="App">
      <form>
        <input onChange={handleChange} value={word} />
        <button onClick={handleSubmit}>Submit</button>
      </form>
      {displayWords()}
    </div>
  );
}

export default App;
