package com.ageandgender.calculationapiservice.messaging;

public class TaskProducerConfiguration extends RabbitMqConfiguration {

    private final String calculateTasksQueue = "calculate.tasks.queue";

    @Override
    protected String getTaskQueueName() {
        return calculateTasksQueue;
    }
}
