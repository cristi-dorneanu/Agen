package com.ageandgender.calculationsearchservice.model.error;

public class CalculationNotFoundException extends RuntimeException {
    public CalculationNotFoundException (Long id) {
        super("Could not find Calculation with id " + id);
    }
}
