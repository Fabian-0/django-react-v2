import React from 'react';

function SelectGender({registerRef, validations, children}) {
  return (
    <div className="col-12 mb-4">

      <select className="form-select" {...registerRef('gender', validations)}>
        <option value='' >Select Gender</option>
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
      </select>

      {children}
    </div>
  )
}

export default SelectGender;