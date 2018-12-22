package com.ageandgender.calculationsearchservice.controller;

import com.ageandgender.calculationsearchservice.model.error.CalculationNotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
public class CalculationNotFoundAdvice {

    @ResponseBody
    @ExceptionHandler(CalculationNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    String CalculationHandler(CalculationNotFoundException exception) {
        return exception.getMessage();
    }
}
