import React,{useState,useEffect} from 'react';
import axios from 'axios';
import './App.css';

const URL_BACKEND = process.env.NODE_ENV === "development" ? "http://localhost:5000" : "";

function App() {
  const [hello, setHello] = useState([]);

  useEffect(() => {
      const stockfetcher = async () => {
          const result = await axios.get(URL_BACKEND+'/hello')
            .then(res => res.data)
          console.log(result)
          setHello(result)
      }
      stockfetcher()
  }, []);
  return (
    <div className="App">
      <div className="App-header">
      <div>My Toke ={window.token} + {process.env.NODE_ENV}</div>
        {
          hello.map((item,key)=><h1 key={key}>{item.title}</h1>)
        }
      </div>
    </div>
  );
}

export default App;
