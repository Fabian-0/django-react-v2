import React from "react";
import GenericInput from "./GenericInput";
import InputErrors from "./InputErrors";
import SelectGender from "./SelectGenderInput";

function FormTemplate({registerRef, errorRef}) {

  const defaultValidations = {required: true, maxLength: 100}

  return(
    <>
      <GenericInput type='text' name='username' registerRef={registerRef} validations={defaultValidations} info='Username' >

        <InputErrors errorRef={errorRef} field='username' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='username' counstraint='maxLength' errorDetail='Max Length 100 Chars' />

      </GenericInput>

      <GenericInput type='text' name='first_name' registerRef={registerRef} validations={defaultValidations} info='First Name' >

        <InputErrors errorRef={errorRef} field='first_name' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='first_name' counstraint='maxLength' errorDetail='Max Length 100 Chars' />

      </GenericInput>

      <GenericInput type='text' name='last_name' registerRef={registerRef} validations={defaultValidations} info='Last Name' >

        <InputErrors errorRef={errorRef} field='last_name' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='last_name' counstraint='maxLength' errorDetail='Max Length 100 Chars' />

      </GenericInput>

      <GenericInput type='email' name='email' registerRef={registerRef} validations={defaultValidations} info='Email' >

        <InputErrors errorRef={errorRef} field='email' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='email' counstraint='maxLength' errorDetail='Max Length 100 Chars' />

      </GenericInput>
        <GenericInput type='url' name='avatar' registerRef={registerRef} validations={{required: true, maxLength: 255}} info='Avatar url' >

        <InputErrors errorRef={errorRef} field='avatar' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='avatar' counstraint='maxLength' errorDetail='Max Length 255 Chars' />

      </GenericInput>

      <GenericInput type='number' name='phone_number' registerRef={registerRef} validations={ {required: true, maxLength: 15}} info='Number phone' >

        <InputErrors errorRef={errorRef} field='phone_number' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='phone_number' counstraint='maxLength' errorDetail='Max Length 15 Chars' />

      </GenericInput>

      <GenericInput type='password' name='password' registerRef={registerRef} validations={ {required: true, maxLength: 15}} info='Password' >

        <InputErrors errorRef={errorRef} field='password' counstraint='required' errorDetail='Field Required' />
        <InputErrors errorRef={errorRef} field='password' counstraint='maxLength' errorDetail='Max Length 15 Chars' />

      </GenericInput>

      <SelectGender registerRef={registerRef} validations={{required: true}} >

        <InputErrors errorRef={errorRef} field='gender' counstraint='required' errorDetail='Field Required' />

      </SelectGender>
    </>
  )
}

export default FormTemplate;