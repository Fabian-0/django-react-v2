import React from "react";

function FormError({ error }) {
  return (
    <div className="alert alert-warning my-3" role="alert">
      <span>{error}</span>
    </div>
  )
};

export default FormError;