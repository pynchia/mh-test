from datetime import datetime
import pytest
from unittest.mock import patch
from mh.pv.pv_power import PV


def test_loading_of_PV_day_power():
    """
    Load the file of daily power samples and check it is ok
    """

@pytest.fixture
def narrow_power_range():
    return (0, 2)

def test_generator_downward(narrow_power_range):
    """
    Test the generated values are stopping at the bottom of the range
    """
    with patch('random.randint', side_effect=lambda a,b: -1):
        range_min, range_max = narrow_power_range
        for msg in it.islice(generate_msgs(range_min, range_max), 0, 5):
            pass
        power = Message.parse(msg).power
        assert power == range_min

def test_generator_upward(narrow_power_range):
    """
    Test the generated values are stopping at the top of the range
    """
    with patch('random.randint', side_effect=lambda a,b: 1):
        range_min, range_max = narrow_power_range
        for msg in it.islice(generate_msgs(range_min, range_max), 0, 5):
            pass
        power = Message.parse(msg).power
        assert power == range_max

def test_generator_continuous():
    """
    Test the generated power signal for continuity (delta must be one)
    """
    RANGE_MAX = 100
    prev_value = RANGE_MAX // 2
    for msg in it.islice(generate_msgs(0, RANGE_MAX), 0, 42):
        curr_value = Message.parse(msg).power
        assert curr_value - prev_value <= 1
        prev_value = curr_value

