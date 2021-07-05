import React from "react";
import { Link } from "react-router-dom";

function MainStudent({ children, classes, handleDelete }) {
  return (
    <div className="row p-2">
      <div className="row">
        <Link className="fs-3 d-inline-block text-decoration-none text-end mt-2" to="/classes/" > Join a class</Link>
      </div>
      <h2>My Classes</h2>
        <ul className="list-group">
        {classes && 
          classes.map(
            element =>  
            (<li key={element.id} className="list-group-item d-flex justify-content-between align-items-center">
              <span>{element.name}</span>
              <div className="buttons">
                <button className="btn btn-warning border-0 py-1 px-3 d-inline-block ms-1" onClick={() => handleDelete(element.id)} >Left</button>
              </div>
            </li>)
            )
          }
        </ul>
        {children}
    </div>
  )
}

export default MainStudent;