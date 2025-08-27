import logo from './logo.svg';
import './App.css';
/*
import Homepage from './views/Homepage'
import Registerpage from './views/Registerpage'
import Loginpage from './views/Loginpage'
import Dashboard from './views/Dashboard'
*/
import Navbar from './views/Navbar'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
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
