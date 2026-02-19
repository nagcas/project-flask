import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/hello')
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return (
    <>
      <h1>Fronted React</h1>
      <p>{message}</p>
    </>
  );
}

export default App;
