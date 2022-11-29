import { Component } from 'react';

const InputZipCode = (props) => {
  const handleZipCode = () => {
    const inputZipCode = document.getElementById('input-zipcode');
    // console.log(inputZipCode);

    console.log(inputZipCode.value);
    props.updateZipCode(inputZipCode.value);
  };

  return (
    <div>
      <hr />
      <div>
        <label>Enter Zip Code: </label>
        <input id="input-zipcode" placeholder="zip code" />
        <button onClick={handleZipCode}>{props.buttonText}</button>
      </div>
      <hr />
    </div>
  );
};

class InputZipCode1 extends Component {
  // handlers
  handleZipCode = () => {
    const inputZipCode = document.getElementById('input-zipcode');
    console.log(inputZipCode.value);
    this.props.updateZipCode(inputZipCode.value);
  };

  // render
  render() {
    return (
      <div>
        <hr />
        <div>
          <label>Enter Zip Code: </label>
          <input id="input-zipcode" placeholder="zip code" />
          <button onClick={this.handleZipCode}>{this.props.buttonText}</button>
        </div>
        <hr />
      </div>
    );
  }
}

export default InputZipCode;
