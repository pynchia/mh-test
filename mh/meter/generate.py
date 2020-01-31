from datetime import datetime
import json
import random as ra


MIN_POWER = 0
MAX_POWER = 9000


def generate_msgs(min_power=MIN_POWER, max_power=MAX_POWER):
    """
    Generate messages with random continuous values (in Watts)
    The msg format is the json:
    {
        "timestamp": timestamp,
        "power": current power level
    }
    """

    curr_value = (max_power - min_power) // 2  # start in the middle

    def update_value():
        """
        update current power value randomly
        """
        nonlocal curr_value

        curr_value += ra.randint(-1, 1)
        if curr_value < min_power:
            curr_value = min_power
        elif curr_value > max_power:
            curr_value = max_power

    while True:
        update_value()
        msg = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "power": curr_value
        }
        yield json.dumps(msg)
