import { BASE_URL, AuthSesion, headers, ValidateStatus } from './Api'

export const CrudClass = async ({ data, history, method, url }) => {
  const isSessionValid = await AuthSesion();
  if(!isSessionValid) {
    return history.replace('/')
  }
  const response = await fetch(`${BASE_URL}${url}`, {
    method,
    headers: headers.auth(isSessionValid),
    body: data,
  })
  const result = await ValidateStatus(response);

  if(result) return result;
  return false;
}

export const GetClasses = async (url) => {
  const response = await fetch(`${BASE_URL}${url}`)

  const result = await ValidateStatus(response);

  if(result) return result;
  return false;
}