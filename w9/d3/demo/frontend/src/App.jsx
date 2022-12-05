// import { useState } from "react";
// import reactLogo from "./assets/react.svg";
// components
import Homepage from "./pages/HomePage";
import NavBar from "./components/NavBar";

import { HashRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import CategoryPage from "./pages/CategoryPage";
import ItemPage from "./pages/ItemPage";
// import getCookie from "./js/utils";

function App() {
  // const [count, setCount] = useState(0);

  return (
    <div className="App">
      <Router>
        <NavBar />

        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/categories" element={<CategoryPage />} />
          <Route path="/items" element={<ItemPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
