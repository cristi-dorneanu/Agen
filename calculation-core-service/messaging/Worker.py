from messaging.Config import RabbitMqConnection
from messaging.TaskProducer import CalculationResultPublisher
from model.Calculation import CalculationResult
import json


class CalculationWorker(RabbitMqConnection):
    def __init__(self):
        super(CalculationWorker, self).__init__()

        self.calculation_result_publish_queue = CalculationResultPublisher(self.connection, self.channel)

        self.queue_name = 'calculate.tasks.queue'

        #todo remove the delete when ready for prod
        self.channel.queue_delete(queue=self.queue_name)
        self.calculation_tasks_queue = self.channel.queue_declare(queue=self.queue_name, durable=True)

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        task = json.loads(body)

        calculation_result = CalculationResult()
        calculation_result.calculationId = task['calculationId']
        calculation_result.estimatedAge = 15

        ch.basic_ack(delivery_tag=method.delivery_tag)
        self.calculation_result_publish_queue.publish_calculation_result(calculation_result)

    def listen_for_messages(self):
        self.channel.basic_consume(self.callback, queue=self.queue_name)
        self.channel.start_consuming()
