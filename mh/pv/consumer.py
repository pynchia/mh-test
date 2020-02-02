"""
The functionality to process the incoming messages
"""

import array
import json
import logging
from datetime import datetime
from mh.broker.services.message import Message, TIMESTAMP_FORMAT
from pv_power import PV


log = logging.getLogger()


class MSG_DECODE_ERROR(Exception):
    pass


class Processor:
    """
    Process the incoming messages from the broker.
    Its output is appended to the given file
    It is a context manager, in order to guarantee closing the output file.
    """

    def __init__(self, output_filename):
        self.output_file = output_filename and open(output_filename, "a")

    def __call__(self, msg):
        """
        Process the incoming msg from the meter
        """
        log.info(f"Received msg {msg}")
        try:
            message = Message.parse(msg)
        except MSG_DECODE_ERROR as e:
            log.error(e)
            out_str = e
        else:
            pv_power = PV.measure_pv_power(message.timestamp)
            total_power = pv_power + message.power
            out_str = f"{message.timestamp} meter={message.power} pv={pv_power}, total={total_power}\n"

        log.info(f"Built msg {out_str.rstrip()}")
        if self.output_file:
            self.output_file.write(out_str)
            log.info(f"Appended msg {out_str}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.output_file:
            self.output_file.close()
