package com.ageandgender.calculationapiservice.messaging;

import org.springframework.beans.factory.annotation.Autowired;

public class CalculationProducer {

    @Autowired
    private TaskProducerConfiguration taskProducerConfiguration;

    public void sendTask(String message) {
        taskProducerConfiguration.rabbitTemplate().convertAndSend(taskProducerConfiguration.getTaskQueueName(), message);
    }
}
