from datetime import datetime
import json
import random as ra


MIN_POWER = 0
MAX_POWER = 9000


def generate_msgs():
    """
    Generate messages with random continuous values (in Watts)
    The msg format is the json:
    {
        "timestamp": timestamp,
        "power": current power level
    }
    """

    curr_value = (MAX_POWER - MIN_POWER) // 2

    def update_value():
        """
        update current power value randomly
        """
        nonlocal curr_value

        curr_value += ra.randint(-1, 1)
        if curr_value < MIN_POWER:
            curr_value = MIN_POWER
        elif curr_value > MAX_POWER:
            curr_value = MAX_POWER

    while True:
        update_value()
        msg = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "power": curr_value
        }
        yield json.dumps(msg)
