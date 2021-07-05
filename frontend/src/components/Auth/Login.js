import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { AlertDangerous } from "../helpers/Alerts";
import { Link, useHistory } from "react-router-dom";
import { Login as Auth, AuthSesion } from "../../Api/Api";
import FormError from '../Form/FormInputError';

function Login() {
  const [requestError, setRequestError] = useState(false);
  const {register, handleSubmit, formState: { errors }} = useForm();
  let history = useHistory();

  useEffect(()=>{
    
    AuthSesion()
      .then(res => {
        
        if(res) {
          const user = JSON.parse(window.localStorage.getItem('user'));
          const rol = (user?.professor) ? 'professor' : (user?.student) ? 'student' : false; 
          if(!rol) {
            return window.localStorage.clear();
          }
          const url = `/profile/${rol}/${user.id}`
          return history.replace(url);
        }
        return;
      })
    
  },[]);

  const onSubmit = async (data) => {
    const isUser = await Auth(data) 
    if (!isUser) return setRequestError(true);
    
    if(isUser) {
      return history.replace(isUser);
    }
    return setRequestError(true);
  }

  return (
    <>
      {requestError && <AlertDangerous alertText="Wrong Username or Password" />}
      <form action="/api/token/" className="row col-lg-8 mx-auto my-4 border border-secondary p-4 rounded-3" onSubmit={handleSubmit(onSubmit)} method="POST">
        <h2 className="text-center">Login</h2>

        <div className="col-12">

          <input type="text" {...register('username', {required: true, maxLength: 100})} className="form-control" placeholder="Email or Username" />

          {errors.username?.type === 'required' && <FormError error={'Field Required'} />}
          {errors.username?.type === 'maxLength' && <FormError error={'Max Length 100 Chars'} />}
        </div>

        <div className="col-12 my-4">

          <input type="password" {...register('password', {required: true, maxLength: 15})} className="form-control" placeholder="Password" />

          {errors.password?.type === 'required' && <FormError error={'Field Required'} />}
          {errors.password?.type === 'maxLength' && <FormError error={'Max Length 15 Chars'} />}
        </div>

        <div className="col-12">

          <select className="form-select" id="autoSizingSelect" {...register('account_type', {required: true})}>
            <option value='' >Select Account Type</option>
            <option value="professor">Professor</option>
            <option value="student">Student</option>
          </select>

          {errors.account_type?.type === 'required' && <FormError error={'Field Required'} />}
        </div>

        <div className="col-12 my-4">
          <button type="submit" className="btn btn-primary m-auto d-block">Log in</button>
        </div>

        <Link to="/register/" className="text-secondary text-decoration-none">Don't you have an account?</Link>
      </form>
    </>
  )
}

export default Login;