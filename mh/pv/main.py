"""
The main module of the PV application
"""

from time import sleep
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from mh.pv.workers import Processor


def main(filename:str, url:str, queue:str):
    rabbit_client = Rabbit(url, queue)
    with Broker(rabbit_client) as broker, Processor(filename) as processor:
        broker.subscribe_and_process(processor=processor)
