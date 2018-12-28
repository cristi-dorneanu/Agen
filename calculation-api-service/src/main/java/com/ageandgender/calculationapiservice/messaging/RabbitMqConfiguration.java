package com.ageandgender.calculationapiservice.messaging;

import org.springframework.amqp.core.AmqpAdmin;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitAdmin;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public abstract class RabbitMqConfiguration {

    @Bean
    public ConnectionFactory getConnectionFactory()
    {
        CachingConnectionFactory connectionFactory = new CachingConnectionFactory("localhost");
        connectionFactory.setUsername("user");
        connectionFactory.setPassword("password");
        return connectionFactory;
    }

    @Bean
    public RabbitTemplate rabbitTemplate()
    {
        RabbitTemplate template = new RabbitTemplate(getConnectionFactory());
        template.setRoutingKey(getTaskQueueName());
        template.setDefaultReceiveQueue(getTaskQueueName());
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

    protected abstract String getTaskQueueName();
}
