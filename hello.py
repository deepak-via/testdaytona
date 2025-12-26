import math


def hello_world():
    """Return a greeting message from E2E Test."""
    return 'Hello from E2E Test 1766585237!'


def pentagon_area(side):
    """
    Calculate the area of a regular pentagon.

    Args:
        side: The length of one side of the pentagon

    Returns:
        The area of the pentagon

    Formula: area = (1/4) * sqrt(25 + 10*sqrt(5)) * side^2
    """
    if side < 0:
        raise ValueError("Side length must be non-negative")

    area = (1/4) * math.sqrt(25 + 10 * math.sqrt(5)) * side ** 2
    return area
