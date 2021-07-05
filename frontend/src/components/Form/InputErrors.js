import React from 'react';
import FormError from './FormInputError';

function InputErrors({ errorRef, field, counstraint, errorDetail }) {
  return (
    errorRef[field]?.type === counstraint && <FormError error={errorDetail} />
  )
}

export default InputErrors;