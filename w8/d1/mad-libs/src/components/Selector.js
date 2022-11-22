import data from '../data/MadLibs';

function Selector(props) {
  // render
  const renderChoices = () => {
    return props.data.map((data, index) => {
      return (
        <option key={index} id={index} value={data.title}>
          {data.title}
        </option>
      );
    }); // implement changes
  };
  const handleChange = (e) => {
    console.log(e);
    props.setSelectedMadLib(props.data[e.target.selectedIndex]);
  };
  return (
    <div id="div-selector">
      <span>Select Story: </span>
      <select onChange={handleChange}>{renderChoices()}</select>
    </div>
  );
}

export default Selector;
