import React from 'react';
// import React, { useState } from 'react';
import GiftImage from '../images/gift.png';

class Door extends React.Component {
  constructor(props) {
    super(props);
    this.state = { opened: false };
    this.toggleDoor = this.toggleDoor.bind(this);
    this.getDoorStateStyle = this.getDoorStateStyle.bind(this);
    this.renderImage = this.renderImage.bind(this);
  }

  toggleDoor() {
    // console.log(this.opened);
    // console.log(this.state.opened);

    if (this.props.result !== null) return;

    this.setState({ opened: !this.state.opened });
    this.props.updateResult(this.props.number);
  }

  getDoorStateStyle() {
    return ' ' + (this.state.opened ? 'door-opened' : 'door-closed');
  }

  renderImage() {
    return this.state.opened && this.props.isPrizeDoor ? (
      <img id="image-prize" src={GiftImage} alt="prize" />
    ) : null;
  }

  render() {
    return (
      <div
        className={'door ' + this.getDoorStateStyle()}
        onClick={this.toggleDoor}
      >
        <div>Door {this.props.number}</div>
        {this.renderImage()}
      </div>
    );
  }
}

// function Door(props) {
//   // states
//   const [opened, setOpened] = useState(false);

//   // events
//   const toggleDoor = () => {
//     if (props.result !== null) return;
//     setOpened((prevOpened) => {
//       return !prevOpened;
//     });
//     props.updateResult(props.number);
//   };

//   // renders
//   const getDoorStateStyle = () => {
//     return ' ' + (opened ? 'door-opened' : 'door-closed');
//   };

//   const renderImage = () => {
//     return opened && props.isPrizeDoor ? (
//       <img id="image-prize" src={GiftImage} alt="prize" />
//     ) : null;
//   };

//   return (
//     <div className={'door ' + getDoorStateStyle()} onClick={toggleDoor}>
//       <div>Door {props.number}</div>
//       {renderImage()}
//     </div>
//   );
// }

export default Door;
