package com.ageandgender.calculationapiservice.api.config;

import com.ageandgender.calculationapiservice.api.model.RabbitMqQueues;
import org.springframework.stereotype.Component;

@Component
public class TaskProducerConfiguration extends RabbitMqConfiguration {

    @Override
    public String getTaskQueueName() {
        return RabbitMqQueues.CALCULATION_RESULT_PRODUCER_QUEUE;
    }
}
