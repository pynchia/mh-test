from typing import Callable


class Broker:
    """
    The broker service
    Each broker instance support one queue only.
    """

    def __init__(self, connector):
        self.connector = connector

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.connector.close()

    def publish(self, msg: str) -> None:
        """
        Publish data to the topic/queue
        """
        self.connector.publish(msg)

    def subscribe_and_consume(self, consumer: Callable) -> None:
        """
        Subscribe to the queue.
        The callback will be called upon each msg received
        """
        self.connector.subscribe(consumer)
        self.connector.consume()
