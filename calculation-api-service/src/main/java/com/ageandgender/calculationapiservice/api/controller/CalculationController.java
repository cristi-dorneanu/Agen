package com.ageandgender.calculationapiservice.api.controller;

import com.ageandgender.calculationapiservice.api.model.entities.Calculation;
import com.ageandgender.calculationapiservice.api.service.CalculateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RefreshScope
@RestController
public class CalculationController {

    @Autowired
    private CalculateService calculateService;

    @PostMapping("/calculate")
    public ResponseEntity calculate(@RequestBody Calculation calculation) {
        return ResponseEntity.ok(calculateService.calculate(calculation));
    }

    @GetMapping("/calculate/{id}")
    public ResponseEntity findCalculation(@PathVariable Long id) {
        Calculation calculation = calculateService.retrieveCalculation(id).orElse(null);
        return ResponseEntity.ok(calculation == null ? new Calculation() : calculation);
    }

}
