import React from "react";
import { Link } from "react-router-dom"; // use Link for handling routing in React 
// Link allows for users to navigate between each page without reloading the application each time
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
      TheraText
      <div className="greeting">Hello valued individual</div>
      </header>
      <div className="App-body">
        <Link to="/page1">
          <button className="nav-button">Employee Portal</button>
        </Link>
        <Link to="/page2">
          <button className="nav-button">Patient Portal</button>
        </Link>
      </div>
    </div>
  );
}

export default App;