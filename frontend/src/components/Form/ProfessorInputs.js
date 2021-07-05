import React from "react";
import GenericInput from "./GenericInput";
import InputErrors from "./InputErrors";

function ProfessorInputs({ errorRef, registerRef}) {
  return (
    <>
      <GenericInput type='text' name='qualification' registerRef={registerRef} validations={{required: true, maxLength: 100}} info='Qualifiction' >

        <InputErrors errorRef={errorRef} field='qualification' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='qualification' counstraint='maxLength' errorDetail='Max Length 100 Chars' />

      </GenericInput>
    </>
  )
}

export default ProfessorInputs;