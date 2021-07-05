import React, { useState } from "react";
import { CrudClass } from '../../Api/Classes';
import ListItemUpdate from './ListItemUpdate';
import ListItem from './ListItem';

function MainProfessor({ data, handlerHistory }) {

  const [className, setClassName] = useState('');
  const [update, setUpdate] = useState(false);
  const [dataUpdate, setDataUpdate] = useState(null);
  const { classroom_set} = data; 
  const dataRequest = {
    history: handlerHistory,
    url: '/classes/'
  }

  const handleRequests = async (id, method) => {
    let classField;
    if(method == 'PATCH') {
      classField = {
        "professor": data.id,
        'name': dataUpdate,
      }
      dataRequest.data = JSON.stringify(classField);
    }
    dataRequest.method = method;
    dataRequest.url += `${id}/` 
    const response = await CrudClass(dataRequest);

    if(!response) return;
    return window.location.reload();
  } 

  const handleAddClass = async () => {
    const classField = {
      'name': className,
    }
    dataRequest.data = JSON.stringify(classField);
    dataRequest.method = 'POST';
    const response = await CrudClass(dataRequest);
    if(!response) return;
    return window.location.reload();
  };

  return (
    <>
      <div className="row">
        <div className="my-2 d-flex">
          <input type="text" name="name"  onChange={(e)=>setClassName(e.target.value)} value={className} placeholder='Class Name' className='form-control w-50 rounded-0 rounded-start' />
          <button type="button" onClick={handleAddClass}  className='btn-primary'>Add</button>
        </div>
      </div>
      <div className="row p-2">
        <h2>My Classes</h2>
        <ul className="list-group">
          {update && 
            classroom_set.map(
              element => (update == element.id) 
                ? <ListItemUpdate key={element.id} handleChange={setDataUpdate} handleUpdate={handleRequests} name={element.name} id={element.id} /> 
                : <ListItem key={element.id} name={element.name} id={element.id} handleDelete={handleRequests} handleEdit={setUpdate} />
              )
          }
          {!update &&
            classroom_set.map(element => (<ListItem key={element.id} name={element.name} id={element.id} handleDelete={handleRequests} handleEdit={setUpdate} />))
          }
        </ul>
      </div>
    </>
  )
}

export default MainProfessor;