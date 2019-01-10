package com.ageandgender.calculationapiservice.api.service;

import com.ageandgender.calculationapiservice.api.model.RabbitMqQueues;
import com.ageandgender.calculationapiservice.api.model.dto.CalculationResult;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CalculationConsumerListener {

    private static final Logger log = LoggerFactory.getLogger(CalculationConsumerListener.class);

    @Autowired
    private CalculateService calculateService;

    @RabbitListener(queues = RabbitMqQueues.CALCULATION_RESULT_CONSUMER_QUEUE)
    public void handleMessage(CalculationResult calculationResult) {
        log.info("Received message as generic: {}", calculationResult.toString());
        calculateService.updateCalculationResult(calculationResult);
    }
}
