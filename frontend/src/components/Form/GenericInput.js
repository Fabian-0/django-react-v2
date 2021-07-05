import React from "react";

function GenericInput({ type, name, registerRef, info, children, validations }) {
  return (
    <div className="col-12 mb-4">

      <input type={type} {...registerRef(name, validations)} className="form-control" placeholder={info} />

      {children}
    </div>
  )
}

export default GenericInput;