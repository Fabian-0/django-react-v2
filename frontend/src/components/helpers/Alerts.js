import React from "react";

export function AlertDangerous({alertText}) {
  return (
    <div className="alert alert-danger d-flex align-items-center my-3" role="alert">
      <div>
        {alertText}
      </div>
    </div>
  )
}