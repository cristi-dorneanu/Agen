import pika
import json
from messaging.Config import RabbitMqConnection


class CalculationResultPublisher(RabbitMqConnection):
    def __init__(self, connection, channel):
        #super(CalculationResultPublisher, self).__init__()

        self.connection = connection
        self.channel = channel
        self.queue_name = 'calculate.result.queue'
        self.calculation_result_queue = self.channel.queue_declare(queue=self.queue_name, durable=True)

    def publish_calculation_result(self, calculation_result):
        result = json.dumps(calculation_result.__dict__)
        properties = pika.BasicProperties(content_type="application/json")
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=result, properties=properties)
        print("Sent message")
