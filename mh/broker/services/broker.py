

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

    def subscribe(self) -> None:
        """
        Subscribe to the queue passed to constructor
        """
        pass

    def read(self) -> str:
        """
        Read data from the topic/queue
        """
        pass
