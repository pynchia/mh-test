import logging
from typing import Callable


log = logging.getLogger()


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

    def publish(self, data: str) -> None:
        """
        Publish data to the topic/queue
        """
        self.connector.publish(data)

    def subscribe_and_process(self, processor: Callable) -> None:
        """
        Subscribe to the queue.
        The callback will be called upon each msg received
        """
        self.connector.subscribe(processor)
        self.connector.consume()
