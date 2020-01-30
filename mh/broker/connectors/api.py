"""
API of the broker connector
it describes the operations allowed on the brokers
independent of kind (e.g. RabbitMQ, MQTT, etc)
"""

from abc import ABC, abstractmethod


class PublishError(Exception):
    pass


class BrokerConnector(ABC):
    """
    Basic interface to a broker every connector must implement
    """

    @abstractmethod
    def publish(self, data: str) -> None:
        """
        Publish data to the topic/queue
        """
        ...

    @abstractmethod
    def subscribe_and_consume(self, callback) -> None:
        """
        Subscribe to the topic/queue passed to constructor
        callback: the worker to which each incoming msg must be passed
        """
        ...



# The nicer/modern way would be
# from typing import Protocol, runtime_checkable
#
# @runtime_checkable
# class Broker(Protocol):
#     """
#     Basic interface to a broker.
#     Each broker instance support one queue only
#     """

#     def publish(self, data: str) -> None:
#         """
#         Publish data to the topic/queue
#         """
#         ...

#     def subscribe(self) -> None:
#         """
#         Subscribe to the topic/queue passed to constructor
#         """
#         ...

#     def read(self) -> str:
#         """
#         Read data from the topic/queue
#         """
#         ...


# def implements(proto: Type):
#     """ Creates a decorator for classes that checks that the decorated class
#     implements the runtime protocol `proto`
#     """

#     def _deco(cls_def):
#         try:
#             assert issubclass(cls_def, proto)
#         except AssertionError as e:
#             e.args = (f"{cls_def} does not implement protocol {proto}",)
#             raise
#         return cls_def

#     return _deco
