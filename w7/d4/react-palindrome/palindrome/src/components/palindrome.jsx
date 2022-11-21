import { useState } from 'react';

function Palindrome() {
  const [text, setText] = useState('');

  const handleChange = (e) => {
    setText(e.target.value);
  };

  const handleSubmit = () => {
    isPalindrome(text);
  };

  const result = isPalindrome(text) ? (
    <h3 className="green">{text} is a palindrome</h3>
  ) : (
    <h3 className="green">
      {text} is <span className="red">not</span> a palindrome
    </h3>
  );
  return (
    <>
      <input onChange={handleChange} value={text}></input>
      {/* <button onClick={handleSubmit}>Submit</button> */}
      {text.length > 0 ? result : ''}
    </>
  );
}

const isPalindrome = (word) => {
  word = word.toLowerCase();
  const pattern = /\W/g;

  word = word.replaceAll(pattern, '');
  // console.log(word);
  return word === [...word].reverse().join('');
};
export default Palindrome;
