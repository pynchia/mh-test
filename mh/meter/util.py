
import random as ra


def generate_value(
    minimum: int = 0,
    maximum: int = 9000
):
    curr_value = (maximum - minimum) // 2
    while True:
        curr_value += ra.randrange(-1, 2)
        if curr_value < minimum:
            curr_value = minimum
        yield curr_value
