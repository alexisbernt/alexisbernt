import React from "react";
import { Link } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">Bright Green Header</header>
      <div className="App-body">
        <Link to="/page1">
          <button className="nav-button">Go to Page 1</button>
        </Link>
        <Link to="/page2">
          <button className="nav-button">Go to Page 2</button>
        </Link>
      </div>
    </div>
  );
}

export default App;