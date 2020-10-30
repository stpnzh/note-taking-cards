import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const fetchURL = 'http://127.0.0.1:8000/notes/'

const App = () => {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const response = await axios.get(fetchURL);
    setData(await response.data);
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>
          {data.map(i => <li>{i.desc}</li>)}
        </p>
      </header>
    </div>
  );
}

export default App;
