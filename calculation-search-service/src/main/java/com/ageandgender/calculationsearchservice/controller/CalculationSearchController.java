package com.ageandgender.calculationsearchservice.controller;

import com.ageandgender.calculationsearchservice.model.entities.Calculation;
import com.ageandgender.calculationsearchservice.model.error.CalculationNotFoundException;
import com.ageandgender.calculationsearchservice.repository.CalculationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RefreshScope
@RestController
public class CalculationSearchController {

    @Autowired
    private CalculationRepository repository;

    @RequestMapping("/calculations/{id}")
    public Calculation findById (@PathVariable Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new CalculationNotFoundException(id));
    }

    @RequestMapping("/calculations")
    public List<Calculation> findAll() {
        return repository.findAll();
    }

    @PostMapping("calculations")
    public Calculation saveCalculation(@RequestBody Calculation calculation) {
        return repository.save(calculation);
    }


}
