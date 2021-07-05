import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { useHistory } from "react-router-dom";
import { AlertDangerous } from "../helpers/Alerts";
import ProfessorInputs from "../Form/ProfessorInputs";
import SubmitInput from '../Form/SubmitInput'
import FormTemplate from "../Form/FormTemplate";

function Register() {

  const { register, handleSubmit, formState: { errors } } = useForm();
  const [requestError, setRequestError] = useState(false);
  const [accountType, setAccountType] = useState(null);

  let history = useHistory()

  const onSubmit = async (data) => {
    const sendData = {
      "username": data.username,
      "first_name": data.first_name,
      "last_name": data.last_name,
      "email": data.email,
      "password": data.password,
    }
    if(accountType == 'professor') {
      sendData.professor = {
        "phone_number": data.phone_number,
        "avatar": data.avatar,
        "gender": data.gender,
        "qualification": data.qualification
      }
    } else {
      sendData.student = {
        "phone_number": data.phone_number,
        "avatar": data.avatar,
        "gender": data.gender,
      }
    }
    const response = await fetch(`/${accountType}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(sendData),
    })
    if(response.status !== 201) return setRequestError(true)
    alert('Succes!')
    return history.replace('/');
  }
  
  return (
    <>
      {!accountType && 
        <div className="row col-lg-8 mx-auto my-4 border border-secondary p-4 rounded-3">
          <h2 className="text-center">Account type...</h2>
          <button onClick={()=>setAccountType('professor')} className="btn btn-outline-dark mb-4">Professor</button>
          <button onClick={()=>setAccountType('student')} className="btn btn-outline-dark">Student</button>
        </div>
      }
      {requestError && <AlertDangerous alertText='User already exists' />}
      {accountType &&
        <form action="/register/" className="row col-lg-8 mx-auto my-4 border border-secondary p-4 rounded-3" onSubmit={handleSubmit(onSubmit)} method="POST">
          <h2 className="text-center">Register</h2>
          <FormTemplate registerRef={register} errorRef={errors} />
          { accountType === 'professor' && <ProfessorInputs errorRef={errors} registerRef={register} />}
          <SubmitInput />

        </form>

      }
      
    </>
  );
}

export default Register;