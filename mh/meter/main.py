"""
The main module of the Meter application
"""

import logging
from time import sleep
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from .generate import generate_msgs


log = logging.getLogger()


def main(url: str, queue: str):
    rabbit_client = Rabbit(url, queue)
    with Broker(rabbit_client) as broker:
        for msg in generate_msgs():
            broker.publish(msg)
            sleep(2) # delay a bit to see things happen
