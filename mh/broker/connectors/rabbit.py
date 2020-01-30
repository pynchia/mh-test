import logging
import pika

from .api import Broker


logging.basicConfig()


# the nicer/modern way would be
# @implements(Broker)
# class Rabbit:
class Rabbit(Broker):
    """
    The RabbitMQ concrete implementation of a broker
    """

    def __init__(self,
            url: str,
            queue: str = ''):
        """
        url: where to connect, i.e. where the broker is
        queue: the topic queue, one only
        """
        # self.url = url
        self.queue = queue
        self.params = pika.URLParameters(url)
        self.params.socket_timeout = 5
       
    def __enter__(self):
        self.connection = pika.BlockingConnection(self.params) # Connect to CloudAMQP
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue=self.queue) # Declare a queue
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def publish(self, data: str):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body='User information'
        )

    def subscribe(self):
        pass

    def read(self):
        pass
