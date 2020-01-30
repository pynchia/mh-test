import logging
import pika
import pika.exceptions as exc
from .api import BrokerConnector, PublishError


logging.basicConfig()


# the nicer/modern way would be
# @implements(Broker)
# class Rabbit:
class Rabbit(BrokerConnector):
    """
    The RabbitMQ concrete implementation of a broker connector
    """

    def __init__(self,
            url: str,
            queue: str = ''):
        """
        url: where to connect, i.e. where the broker is
        queue: the topic queue, one only for now
        """
        # self.url = url
        self.queue = queue
        params = pika.URLParameters(url)
        params.socket_timeout = 5
        self.connection = pika.BlockingConnection(params) # connect
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue=self.queue) # declare the queue
    
    def close(self):
        self.connection.close()

    def publish(self, data: str):
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue,
                body=data
            )
        except (
            exc.UnroutableError,
            exc.NackError
            ) as err:
            raise PublishError(err)

    def subscribe(self):
        pass

    def read(self):
        pass
