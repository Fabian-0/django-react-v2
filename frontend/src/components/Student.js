import React, { useEffect, useState } from "react";
import { useHistory } from "react-router";
import Navbar from "./Layout/Navbar";
import MainStudent from "./Layout/MainStudent";
import { AuthSesion } from '../Api/Api'
import { CrudClass } from "../Api/Classes";


function Student() {

  let history = useHistory()
  let [studentData, setStudentData] = useState(false);
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
        return setStudentData(data);
      })
  }, []); 

  const handleDelete = async (id) => {
    const response = await CrudClass({history, method: 'DELETE', url: `/student/${id}/classes/`});
    if(response) return window.location.reload();
    return alert('An expected error, try again!');
  }

  return (
    <>
      {studentData && 
        <>
          <Navbar data={
            {username: studentData.username, 
            avatar: studentData.student.avatar, 
            first_name:studentData.first_name}
            }
            handleHistory={history} />
          <MainStudent handlerHistory={history} classes={studentData.student.classes} handleDelete={handleDelete} />
        </>
      }
    </>
  )
}

export default Student;