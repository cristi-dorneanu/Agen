package com.ageandgender.calculationapiservice.messaging;

import org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer;
import org.springframework.amqp.rabbit.listener.adapter.MessageListenerAdapter;
import org.springframework.context.annotation.Bean;

public class CalculationResultConsumerConfiguration extends RabbitMqConfiguration{

    private final String calculateResultsConsumerQueue = "calculate.result.queue";

    @Override
    protected String getTaskQueueName() {
        return null;
    }

    @Bean
    public SimpleMessageListenerContainer listenerContainer() {
        SimpleMessageListenerContainer container = new SimpleMessageListenerContainer();
        container.setConnectionFactory(getConnectionFactory());
        container.setQueueNames(calculateResultsConsumerQueue);
        container.setMessageListener(getMessageListenerAdapter());
        return container;
    }

    @Bean
    public MessageListenerAdapter getMessageListenerAdapter() {
        return new MessageListenerAdapter();
    }
}
