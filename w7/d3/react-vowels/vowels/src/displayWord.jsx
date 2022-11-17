function DisplayWord(props) {
  const vowels = /[aeiou]/gi;
  // console.log(props.word.match(vowels));
  let returnHTML = [];
  for (let letter of props.word) {
    if (letter.match(vowels)) {
      returnHTML.push(<span className="vowel">{letter}</span>);
    } else {
      returnHTML.push(letter);
    }
  }

  return <h1>{returnHTML.map((letter) => letter)}</h1>;
}

export default DisplayWord;
