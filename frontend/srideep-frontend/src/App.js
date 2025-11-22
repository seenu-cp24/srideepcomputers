import React from "react";
import "./App.css";
import TestAPI from "./components/TestAPI"; // Import the API test component
import logo from './logo.svg';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* React logo */}
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to SRI DEEP COMPUTERS
        </p>

        {/* Test API Component */}
        <TestAPI />

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
