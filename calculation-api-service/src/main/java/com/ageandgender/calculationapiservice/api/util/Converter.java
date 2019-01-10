package com.ageandgender.calculationapiservice.api.util;

import com.ageandgender.calculationapiservice.api.model.dto.Task;
import com.ageandgender.calculationapiservice.api.model.entities.Calculation;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Optional;

@Component
public class Converter {

    @Autowired
    private ObjectMapper objectMapper;

    public Optional<String> dtoToJson(Object dto) {
        try {
            return Optional.of(objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(dto));
        } catch(JsonProcessingException e) {

        }

        return Optional.empty();
    }


    public Task entityToDto(Calculation calculation) {
        Task task = new Task();

        task.setCalculationId(calculation.getId());
        task.setCalculationType(calculation.getType());
        task.setImage(calculation.getImage());

        return task;
    }
}
