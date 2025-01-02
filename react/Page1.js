import React from "react";
import { Link } from "react-router-dom";
import "./App.css";

function Page1() {
  return (
    <div className="Page">
      <h1>Welcome to Page 1</h1>
      <Link to="/">
        <button className="nav-button">Go Back to Home</button>
      </Link>
    </div>
  );
}

export default Page1;