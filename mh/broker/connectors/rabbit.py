import logging
import pika
import pika.exceptions as exc
from .api import BrokerConnector, PublishError


log = logging.getLogger()


# the nicer/modern way would be
# @implements(Broker)
# class Rabbit:
class Rabbit(BrokerConnector):
    """
    The RabbitMQ concrete implementation of a broker connector
    """

    def __init__(self,
            url: str,
            queue: str = ''
        ):
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

    def publish(self, msg: str):
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue,
                body=msg
            )
            log.info(msg)
        except (
            exc.UnroutableError,
            exc.NackError
            ) as err:
            raise PublishError(err)

    def subscribe(self, callback):
        self.callback = callback
        self.channel.basic_consume(
            self.queue,
            self._receive_msg,
            auto_ack=True)

    def consume(self):
        self.channel.start_consuming()

    def _receive_msg(self, ch, method, properties, body):
        self.callback(body)
