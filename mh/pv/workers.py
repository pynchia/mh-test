"""
The functionality to process the incoming messages
"""

import array
import json
import logging
from datetime import datetime
from typing import NamedTuple


log = logging.getLogger()

SECS_IN_A_DAY = 86400
NUM_SAMPLES = 4320  # it can be smaller, e.g. 432, the curve would still be good
PV_SCALE = SECS_IN_A_DAY // NUM_SAMPLES

# Here is how I created the file with the PV power samples
#
# MU = 3
# VARIANCE = 1
# SIGMA = math.sqrt(VARIANCE)
# PV_DAY_TIME_SAMPLES = np.linspace(0, MU + 3*SIGMA, NUM_SAMPLES)  # secs in a day, scaled down
# PV_DAY_POWER = (stats.norm.pdf(PV_DAY_TIME_SAMPLES, MU+0.5, SIGMA-0.5)*4125).astype(int) # 3.3KW is the max
# np.savetxt('PV_DAY_POWER.txt', PV_DAY_POWER, fmt='%u')


PV_DAY_POWER_FILENAME = 'PV_DAY_POWER.txt'

def load_PV_DAY_POWER(filename):
    with open(filename) as f:
        for val in f:
            yield int(val)

PV_DAY_POWER = array.array('L', load_PV_DAY_POWER(PV_DAY_POWER_FILENAME))


def measure_pv_power(when):
    """
    Measure the power output of the PV at the specified datetime
    It assumes the PV output is the same each day
    Return: PV power output
    """
    seconds_since_midnight = int(
        (when - when.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    )
    return PV_DAY_POWER[seconds_since_midnight // PV_SCALE] 

class MSG_DECODE_ERROR(Exception):
    pass

class Processor:
    """
    Process the incoming messages from the broker.
    Its output is appended to the given file
    It is a context manager to guarantee closing the output file.
    """

    def __init__(self, output_filename):
        self.output_file = output_filename and open(output_filename, "a")

    def __call__(self, msg):
        """
        Process the incoming msg from the meter
        """
        try:
            timestamp, meter_power = self.parse_msg(msg)
        except MSG_DECODE_ERROR as e:
            log.error(e)
            out_str = e
        else:
            pv_power = measure_pv_power(timestamp)
            total_power = pv_power + meter_power
            out_str = f"{timestamp} meter={meter_power} pv={pv_power}, total={total_power}\n"

        log.info(out_str)
        if self.output_file is not None:
            self.output_file.write(out_str)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.output_file is not None:
            self.output_file.close()

    @staticmethod
    def parse_msg(msg):
        """
        Parse the incoming message from the meter
        Return:
            timestamp of the message
            power value
        """
        try:
            msg_d = json.loads(msg)
        except json.JSONDecodeError:
            raise MSG_DECODE_ERROR(f"Malformed json message received: {msg}")
        return (
            datetime.strptime(msg_d['timestamp'], '%Y-%m-%d %H:%M:%S'),
            int(msg_d['power'])
        )
