from datetime import datetime, timedelta
import pytest
from unittest.mock import patch
from mh.pv.pv_power import PV


def test_loading_of_PV_day_power():
    """
    Load the file of daily power samples and check it is ok
    """
    PV.load_pv_day_power()
    assert len(PV._PV_DAY_POWER) == PV._NUM_SAMPLES

def test_measure_pv_power():
    PV.load_pv_day_power()
    now = datetime.now()
    midnight_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    pv_power = PV.measure_power(midnight_today)
    assert type(pv_power) == int
    assert pv_power == 0
    pv_power = PV.measure_power(midnight_today+timedelta(days=-1)) # midnight yesterday
    assert pv_power == 0
    pv_power = PV.measure_power(
        midnight_today+timedelta(hours=14)) # at 2pm it peaks
    assert pv_power == max(PV._PV_DAY_POWER)
