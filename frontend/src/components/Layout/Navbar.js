import React from "react";
import { Logout } from '../helpers/functions';

function Navbar({ data, handleHistory }) {

  const {avatar, username, first_name} = data;

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <div className="navbar-brand rounded" style={{height: '60px', width: '60px', overflow: 'hidden'}}>
          <img className="w-100" src={avatar} alt={username} />
        </div>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <p className="nav-link active" aria-current="page" href="#">{first_name}</p>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">{username}</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#" onClick={()=>Logout(handleHistory)}>Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar;