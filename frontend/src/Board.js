import React, {useState} from "react"
import "./Board.css"
import axios from 'axios';

const Board = ({startdate, finishdate, state}) => {
    const [text, setText] = useState([]);

    axios.get("http://127.0.0.1:8000/board/")
        .then((response) => {
        setText([...response.data]);
        })
        .catch(function (error) {
        console.log(error);
        });
    
    const result = text.filter((e) => (e.start === startdate) && (e.finish === finishdate));

    return (
        (state)?(
            (result.length !== 0) ? (
                <div className="Board">
                    <p className="Board--content">startdate :{startdate}, finishdate: {finishdate}</p>
                    <a>{result['0'].word1} : </a><a href = {result['0'].link1} className="Board--content">{result['0'].title1}</a><br></br>
                    <a>{result['0'].word2} : </a><a href = {result['0'].link2} className="Board--content">{result['0'].title2}</a><br></br>
                    <a>{result['0'].word3} : </a><a href = {result['0'].link3} className="Board--content">{result['0'].title3}</a><br></br>
                </div>
            ) : (<p>Is Loading...</p>)
        ) : (<br></br>)
    );
};

export default Board;