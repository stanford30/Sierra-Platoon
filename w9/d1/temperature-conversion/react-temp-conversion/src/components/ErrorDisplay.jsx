import { Component } from "react";
import { useEffect } from "react";

const ErrorDisplay = (props) => {
  useEffect(() => {
    console.log("!! There was an error !!");

    console.log("++ The error was resolved ++");
  }, [props.message]);

  return (
    <div>
      <p className="error">Error: {props.message}</p>
    </div>
  );
};
class ErrorDisplay1 extends Component {
  componentDidMount() {
    console.log("!! There was an error !!");
  }

  componentWillUnmount() {
    console.log("++ The error was resolved ++");
  }

  render() {
    return (
      <div>
        <p className="error">Error: {this.props.message}</p>
      </div>
    );
  }
}

export default ErrorDisplay;
