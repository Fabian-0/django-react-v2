import React from "react";

function ListItem({ handleDelete, handleEdit, id, name }) {
  return(
    <li className="list-group-item d-flex justify-content-between align-items-center"><span>{name}</span> 
      <div className="buttons">
        <button className="btn btn-danger border-0 py-1 px-3 d-inline-block ms-1" onClick={() => handleDelete(id, 'DELETE')}>Delete</button>
        <button className="btn btn-warning border-0 py-1 px-3 d-inline-block ms-1" onClick={() => handleEdit(id)} >Update</button>
      </div>
    </li>
  )
}

export default ListItem;