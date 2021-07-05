import React, { useEffect, useState } from "react";
import { useHistory } from "react-router";
import Navbar from "./Layout/Navbar";
import MainProfessor from "./Layout/MainProfessor";
import { AuthSesion } from '../Api/Api'


function Professor() {

  let history = useHistory()
  let [professorData, setProfessorData] = useState(false);
  let data;
  useEffect(()=>{
    data = window.localStorage.getItem('user');
    if(!data) {
      return history.replace('/');
    };

    AuthSesion()
      .then(res => {
        if(!res) return history.replace('/');
        data = JSON.parse(window.localStorage.getItem('user'));
        return setProfessorData(data);
      })
  }, []); 

  return (
    <>
      {professorData && 
        <>
          <Navbar data={
            {username: professorData.username, 
            avatar: professorData.professor.avatar, 
            first_name:professorData.first_name}
            }
            handleHistory={history} />
          <MainProfessor handlerHistory={history} data={professorData} />
        </>
      }
    </>
  )
}

export default Professor;