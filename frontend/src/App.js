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

  return(
    <div className = 'App'>
      <div class= "row1">
        <div class = "col1">
        <h1>📰News Crawler</h1>
        <h2>📅StartDate와 📅FinishDate를 입력하면 
          <br></br>그 기간동안 뉴스에서 자주 언급된 단어들과 
          <br></br>뉴스 기사를 보여줍니다.
        </h2>
        </div>
        <div class = "col2">
          <h3 class="pb-3">Date Input</h3>
          <div class="form-style">
            <form>
              <div class="form-group pb-3">
                <input
                  value = {startdate}
                  placeholder = "Start Date : YYYYMMDD"
                  name = "startdate"
                  onChange = {changed}
                ></input>
              </div>
              <div class="form-group pb-3">
                <input
                  value = {finishdate}
                  placeholder = "Finish Date : YYYYMMDD"
                  name = "finishdate"
                  onChange = {changed}
                ></input>
              </div>
              <div class = 'pb-2'>
                <button type='button' class="w-btn w-btn-gra1" onClick = {clickHandler_crawl}>⛏Crawl News</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="row2">
        <Board startdate={startdate} finishdate={finishdate} state={state}/>
      </div>
    </div>
  );
};

export default App;
