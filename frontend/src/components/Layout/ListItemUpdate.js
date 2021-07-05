import React from "react";

function ListItemUpdate({ handleChange, handleUpdate, name, id }) {
  return (
    <li className="list-group-item d-flex justify-content-between align-items-center"><input type="text" name="update" onChange={(e) => handleChange(e.target.value)} defaultValue={name}  /> 
      <div className="buttons">
        <button className="btn btn-warning border-0 py-1 px-3 d-inline-block ms-1" onClick={() => handleUpdate(id, 'PATCH')} >Update</button>
      </div>
    </li>
  )
}

export default ListItemUpdate;