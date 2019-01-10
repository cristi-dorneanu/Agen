package com.ageandgender.calculationapiservice.api.service;

import com.ageandgender.calculationapiservice.api.model.entities.Calculation;
import com.ageandgender.calculationapiservice.api.config.TaskProducerConfiguration;
import com.ageandgender.calculationapiservice.api.util.Converter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CalculationProducerService {

    @Autowired
    private TaskProducerConfiguration taskProducerConfiguration;

    @Autowired
    private Converter converter;

    public void sendTask(Calculation calculation) {
        taskProducerConfiguration.rabbitTemplate().convertAndSend(taskProducerConfiguration.getTaskQueueName(), converter.entityToDto(calculation));
    }
}
