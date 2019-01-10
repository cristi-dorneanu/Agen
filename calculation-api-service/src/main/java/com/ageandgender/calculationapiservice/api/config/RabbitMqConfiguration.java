package com.ageandgender.calculationapiservice.api.config;

import org.springframework.amqp.core.AmqpAdmin;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitAdmin;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.support.converter.Jackson2JsonMessageConverter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public abstract class RabbitMqConfiguration {

    @Bean
    public ConnectionFactory getConnectionFactory()
    {
        return new CachingConnectionFactory("localhost");
    }

    @Bean
    public RabbitTemplate rabbitTemplate()
    {
        RabbitTemplate template = new RabbitTemplate(getConnectionFactory());
        template.setRoutingKey(getTaskQueueName());
        template.setDefaultReceiveQueue(getTaskQueueName());
        template.setMessageConverter(getMessageConverter());
        return template;
    }

    @Bean
    public AmqpAdmin amqpAdmin()
    {
        return new RabbitAdmin(getConnectionFactory());
    }

    @Bean
    public Queue tasksQueue()
    {
        return new Queue(getTaskQueueName());
    }

    @Bean
    public Jackson2JsonMessageConverter getMessageConverter() {
        return new Jackson2JsonMessageConverter();
    }

    protected abstract String getTaskQueueName();
}
