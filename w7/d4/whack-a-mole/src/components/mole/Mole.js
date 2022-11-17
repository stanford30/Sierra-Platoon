import './Mole.css';
import MoleIcon from './Mole.svg';

function Mole(props) {
  return (
    <div className="den">
      <img
        src={MoleIcon}
        // className="Mole"
        alt="Mole"
        className={props.isMoleVisible ? 'visible' : 'not-visible'}
        onClick={props.isMoleVisible ? props.onMoleWhacked : null}
      />
    </div>
  );
}

export default Mole;
