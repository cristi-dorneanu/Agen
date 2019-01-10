package com.ageandgender.calculationapiservice.api.model;

public interface RabbitMqQueues {
    String CALCULATION_RESULT_CONSUMER_QUEUE = "calculate.result.queue";
    String CALCULATION_RESULT_PRODUCER_QUEUE = "calculate.tasks.queue";
}
