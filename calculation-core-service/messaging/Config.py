
class RabbitMqConnection:
    def __init__(self, host='localhost', user='user', password='password'):
        self.host = host
        self.user = user
        self.password = password

        self.init_connection()

    def init_connection(self):
        pass
