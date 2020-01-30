
import random as ra

SCALE = 100

def generate_values(minimum: int = 0, maximum: int = 9000):
    """
    Generate random values in the range given, starting at the middle
    """

    curr_value = (maximum - minimum) // 2
    while True:
        curr_value += ra.randint(-SCALE, SCALE) // SCALE
        if curr_value < minimum:
            curr_value = minimum
        elif curr_value > maximum:
            curr_value = maximum
        yield curr_value
