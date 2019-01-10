package com.ageandgender.calculationapiservice.api.controller;

import com.ageandgender.calculationapiservice.api.model.entities.Calculation;
import com.ageandgender.calculationapiservice.api.service.CalculateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.*;

import javax.ws.rs.core.Response;

@RefreshScope
@RestController
public class CalculationController {

    @Autowired
    private CalculateService calculateService;

    @PostMapping("/calculate")
    public Response calculate(@RequestBody Calculation calculation) {
        return Response.ok(calculateService.calculate(calculation)).build();
    }

    @GetMapping("/calculate/{id}")
    public Response findCalculation(@PathVariable Long id) {
        Calculation calculation = calculateService.retrieveCalculation(id).orElse(null);
        return Response.ok(calculation).build();
    }

}
