package com.ageandgender.calculationapiservice.api.config;

import com.ageandgender.calculationapiservice.api.model.RabbitMqQueues;
import org.springframework.stereotype.Component;

@Component
public class CalculationResultConsumerConfiguration extends RabbitMqConfiguration {

    @Override
    protected String getTaskQueueName() {
        return RabbitMqQueues.CALCULATION_RESULT_CONSUMER_QUEUE;
    }

}
