import { useState } from 'react';
import Door from './Door';

function Game(props) {
  // states
  const [prizeDoor /*setPrizeDoor*/] = useState(
    Math.floor(Math.random() * props.numDoors) + 1
  );
  const [result, setResult] = useState(null);

  // events
  const updateResult = (door) => {
    if (result !== null) return;

    setResult(door === prizeDoor);
  };

  const startNewGame = () => {
    window.location.reload();
  };

  // renders
  const renderDoors = () => {
    let doorElements = [];
    for (let i = 1; i <= props.numDoors; i++) {
      doorElements.push(
        <Door
          key={i}
          number={i}
          isPrizeDoor={i === prizeDoor}
          updateResult={updateResult}
          result={result}
        />
      );
    }
    return doorElements;
  };

  const renderResult = () => {
    if (result === null) return '';

    return result ? (
      <p className="result-win">You win!!!</p>
    ) : (
      <p className="result-lose">You lose!!</p>
    );
  };

  return (
    <div className="center-container">
      <h3>Choose a door:</h3>
      <div id="door-container">{renderDoors()}</div>
      <div>
        <button className="btn" onClick={startNewGame}>
          New Game
        </button>
      </div>
      <div>{renderResult()}</div>
    </div>
  );
}

export default Game;
