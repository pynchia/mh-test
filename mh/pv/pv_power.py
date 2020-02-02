"""
The functionality of the PV panel
"""
import array
from datetime import datetime
import logging


log = logging.getLogger()


class PV:
    _SECS_IN_A_DAY = 86400
    _NUM_SAMPLES = 4320  # it can be smaller, e.g. 432, the curve would still be good
    _PV_SCALE = _SECS_IN_A_DAY // _NUM_SAMPLES

    # # The file with the PV power samples was created with:
    # import math
    # import numpy
    # from scipy import stats
    # MU = 3
    # VARIANCE = 1
    # SIGMA = math.sqrt(VARIANCE)
    # PV_DAY_TIME_SAMPLES = np.linspace(0, MU + 3*SIGMA, NUM_SAMPLES)  # secs in a day, scaled down
    # PV_DAY_POWER = (stats.norm.pdf(PV_DAY_TIME_SAMPLES, MU+0.5, SIGMA-0.5)*4125).astype(int) # 3.3KW is the max
    # np.savetxt('PV_DAY_POWER.txt', PV_DAY_POWER, fmt='%u')

    @classmethod
    def load_pv_day_power(cls, filename='PV_DAY_POWER.txt'):
        with open(filename) as f:
            cls._PV_DAY_POWER = array.array('L', map(int, f))
        log.info(f"Loaded PV day power file: {filename}")

    @classmethod
    def measure_pv_power(cls, when: datetime):
        """
        Measure the power output of the PV at the specified datetime
        It assumes the PV output is the same each day
        Return: PV power output
        """
        seconds_since_midnight = int(
            (when - when.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        )
        return cls._PV_DAY_POWER[seconds_since_midnight // cls._PV_SCALE] 
