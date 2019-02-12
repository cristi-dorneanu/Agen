package com.ageandgender.calculationapiservice.api.service;

import com.ageandgender.calculationapiservice.api.model.dto.CalculationResult;
import com.ageandgender.calculationapiservice.api.model.entities.Calculation;
import com.ageandgender.calculationapiservice.api.model.error.CalculationNotFoundException;
import com.ageandgender.calculationapiservice.api.repository.CalculationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class CalculateService {

    @Autowired
    private CalculationProducerService calculationProducerService;

    @Autowired
    private CalculationRepository calculationRepository;

    public Calculation calculate(Calculation calculation) {
        calculationRepository.save(calculation);
        calculationProducerService.sendTask(calculation);

        return calculation;
    }

    public Optional<Calculation> retrieveCalculation(Long id) {
        return calculationRepository.findById(id);
    }

    public void updateCalculationResult(CalculationResult calculationResult) {
        Calculation calculation = new Calculation();

        try {
            calculation = calculationRepository.findById(calculationResult.getCalculationId()).orElseThrow(() -> new CalculationNotFoundException(calculationResult.getCalculationId()));
        } catch (Exception e) {

        }

        calculation.setStatus(calculationResult.getCalculationStatus());
        calculation.setEstimatedAge(calculationResult.getEstimatedAge());
        calculation.setEstimatedGender(calculationResult.getEstimatedGender());
        calculation.setFace(calculationResult.isFace());
        calculation.setErrorMessage(calculationResult.getErrorMessage());

        if(calculationResult.getImage() != null && !calculationResult.getImage().isEmpty()) {
            calculation.setImage(calculationResult.getImage());
        }

        calculationRepository.save(calculation);
    }
}
