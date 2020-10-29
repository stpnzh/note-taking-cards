import { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const items = await fetch('http://127.0.0.1:8000/notes/');
    setData(await items.json());
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>
          {data.map(i => <li>{i.description}</li>)}
        </p>
      </header>
    </div>
  );
}

export default App;
