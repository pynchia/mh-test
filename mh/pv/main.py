"""
The main module of the PV application
"""

from time import sleep
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from mh.pv.consumer import Processor
from mh.pv.pv import PV


def main(out_filename:str, url:str, queue:str):
    PV.load_pv_day_power()
    rabbit_client = Rabbit(url, queue)
    with Broker(rabbit_client) as broker, Processor(out_filename) as processor:
        broker.subscribe_and_consume(consumer=processor)
