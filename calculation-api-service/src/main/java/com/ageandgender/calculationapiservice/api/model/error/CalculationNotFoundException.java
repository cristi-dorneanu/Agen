package com.ageandgender.calculationapiservice.api.model.error;

public class CalculationNotFoundException extends RuntimeException {
    public CalculationNotFoundException (Long id) {
        super("Could not find Calculation with id " + id);
    }
}
