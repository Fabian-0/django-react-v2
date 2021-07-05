import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { AuthSesion } from "../Api/Api";
import { CrudClass } from "../Api/Classes";
import { filterClasses } from "./helpers/functions";

function Classes() {

  let history = useHistory()
  const [classesData, setClassesData] = useState(null)
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
        CrudClass({method: 'GET', url: '/classes/'})
          .then(resClasses => {
            if(!resClasses) return history.replace('/');

            const toJoin = filterClasses({studentClasses:data.student.classes, allClasses: resClasses.results})

            let toReturn = resClasses;
            toReturn.results = toJoin;
            return setClassesData(toReturn);
          })
      })
  }, []); 

  const handleJoin = async (id) => {
    const userId = JSON.parse(window.localStorage.getItem('user'));
    const response = await CrudClass({ data: JSON.stringify({"id":id}),history, method: 'POST', url: `/student/${userId.id}/classes/` })
    if(response) return window.location.reload();
    return alert('An expected error, try again!');
  }

  const handlePagination = async (url) => {
    const response = await CrudClass({ history, method: 'GET', url});
    if(!response) return alert('An expected error, try again!');;
        
    const user =data = JSON.parse(window.localStorage.getItem('user'));
    const filter  = filterClasses({studentClasses: user.student.classes, allClasses: response.results});
    const toReturn = response;
    toReturn.results = filter;
    return setClassesData(toReturn);
  }

  return (
    <>
      <div className="row pt-4">
        <h2>All Classes</h2>
        {classesData &&
        <ul className="list-group mt-4">
            {classesData.results.map((element, index) => (
                <li key={element.id} className="list-group-item d-flex justify-content-between">
                  <span>{element.name}</span>
                  <button onClick={() => handleJoin(element.id)} className="btn btn-success">Join</button>
                </li>
            ))}
        </ul>
        }
      </div>
      <div className="row">
        {classesData?.previous && <button onClick={() => handlePagination(classesData.previous)} className='d-inline'>&#8617;</button>}
        {classesData?.next && <button onClick={() => handlePagination(classesData.next)} >&#x21aa;</button>}
      </div>
    </>
  )
}

export default Classes;