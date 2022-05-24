import './App.css';
import React, { useState } from 'react'
import Board from './Board.js'
import axios from 'axios';

const App = () =>{
  
  const [inputList, setInputList] = useState({startdate : "", finishdate : "" });
  const [state, setState] = useState(false)
  const [text, setText] = useState([]);
  const {startdate, finishdate} = inputList;

  const changed = (e) =>{
    const {value, name} = e.target;
    setInputList({...inputList, [name]: value});
  };

  const clickHandler_crawl = () =>{
    console.log({startdate},{finishdate});
    setState(true);
    axios.post("http://127.0.0.1:8000/user/", {
            startdate: startdate,
            finishdate: finishdate,
          });
  };

  // axios.get("http://127.0.0.1:8000/board/")
  //       .then((response) => {
  //       setText([...response.data]);
  //       })
  //       .catch(function (error) {
  //       console.log(error);
  //       });
    
  // const result = text.filter((e) => (e.start === startdate) && (e.finish === finishdate));
  
  // (result.length !== 0) ? (setState(false)) : (console.log('???'));

  return(
    <div className = 'App'>
      <header>
        <h1>News Crawler</h1>
      </header>
      <input
        value = {startdate}
        placeholder = "StartDate"
        name = "startdate"
        onChange = {changed}
      ></input>
      <input
        value = {finishdate}
        placeholder = "FinishDate"
        name = "finishdate"
        onChange = {changed}
      ></input>
      <br></br>
      <button onClick = {clickHandler_crawl}>Crawl News</button>
      <br></br>
      {(state) ? (
        <p>Is Loading...</p>
      ) : (
        <Board startdate={startdate} finishdate={finishdate}/>
      )}
    </div>
  );
};

export default App;
