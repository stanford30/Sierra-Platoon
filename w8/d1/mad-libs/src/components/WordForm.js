function WordForm(props) {
  // render
  const renderInputs = () => {
    return props.words.map((word, index) => {
      return (
        <input
          onChange={handleChange}
          id={index}
          key={index}
          placeholder={word.label}
        ></input>
      );
    }); // implement changes
  };

  const handleChange = (e) => {
    console.log(props);

    props.updateMadLibWord(e.target.id, e.target.value);
  };

  return <div id="div-words">{renderInputs()}</div>;
}

export default WordForm;
