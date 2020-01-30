"""
The main module of the application
"""

from mh.broker.connectors.rabbit import Rabbit
from .util import generate_value


def main(url: str, queue: str):
    print(f"url = {url}")
    with Rabbit(url, queue) as broker:
        for value in generate_value():
            print(value)
            broker.publish(value)
