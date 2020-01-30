"""
The main module of the Meter application
"""

from time import sleep
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from .util import generate_values


def main(url: str, queue: str):
    rabbit_client = Rabbit(url, queue)
    with Broker(rabbit_client) as broker:
        for value in generate_values():
            print(value)
            broker.publish(str(value))
            sleep(2) # delay a bit to see things happen
