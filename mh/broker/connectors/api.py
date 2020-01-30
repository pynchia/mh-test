"""
API of the broker connector
it describes the operations allowed on the brokers
independent of kind (e.g. RabbitMQ, MQTT, etc)
"""

from abc import ABC, abstractmethod


class Broker(ABC):
    """
    Basic interface to a broker.
    Each broker instance support one queue only
    """

    @abstractmethod
    def __enter__(self) -> None:
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        pass

    @abstractmethod
    def publish(self, data: str) -> None:
        """
        Publish data to the topic/queue
        """
        ...

    @abstractmethod
    def subscribe(self) -> None:
        """
        Subscribe to the topic/queue passed to constructor
        """
        ...

    @abstractmethod
    def read(self) -> str:
        """
        Read data from the topic/queue
        """
        ...


# The nicer/modern way would be
# from typing import Protocol, ContextManager, runtime_checkable, Dict, List
#
# @runtime_checkable
# class Broker(ContextManager):
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
