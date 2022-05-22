import React, {useState} from "react"
import "./BoardAPI.css"

const Board = ({startdate, finishdate}) => {
    const [BoardData, setBoardData] = useState(null)
    const url = 'http://localhost:8000/board/';
    fetch(url).then((res) => res.json())
      .then((data) => {
          console.log(data)
          setBoardData([data]);
    })

    console.log(BoardData)
    
    return (
        <div className="Board">
            <p className="Board--content">{BoardData}</p>
            <p className="Board--content">{BoardData}</p>
        </div>
    );
};

export default Board;