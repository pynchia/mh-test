"""
The main module of the Meter application
"""

from time import sleep
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from .util import generate_value


def main(url: str, queue: str):
    rabbit_client = Rabbit(url, queue)
    with Broker(rabbit_client) as broker:
        for value in generate_value():
            print(value)
            broker.publish(str(value))
            sleep(1) # delay a bit to see things happen
