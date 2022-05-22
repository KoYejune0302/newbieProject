import './App.css';
import React, { useState } from 'react'
import Board from './Board.js'
import axios from 'axios'

const App = () =>{
  
  const [inputList, setInputList] = useState({startdate : "", finishdate : "" });
  const [dataList, setDataList] = useState({startdate : "", finishdate : "" });

  const {startdate, finishdate} = inputList;

  const changed = (e) =>{
    const {value, name} = e.target;
    setInputList({...inputList, [name]: value});
    console.log(inputList);
  };

  const clickHandler_crawl = () =>{
    // fetch('https://localhost:8000/user', {
    //   method: 'post',
    //   body: JSON.stringify({
    //       startdate: {startdate},
    //       finishdate: {finishdate}
    //   })
    // })
    // .then(res => res.json())
    // axios.post("http://127.0.0.1:8000/user", {
    //     startdate: {startdate},
    //     finishdate: {finishdate},
    // })
    console.log({startdate},{finishdate})  
  };

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
      <Board startdate={startdate} finishdate={finishdate} />
    </div>
  );
};

export default App;
