import pika


class RabbitMqConnection:
    def __init__(self, host='localhost', user='user', password='password'):
        self.host = host
        self.user = user
        self.password = password

        self.connection = None
        self.channel = None

        self.init_connection()

    def init_connection(self):
        #credentials = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(host=self.host)

        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()
