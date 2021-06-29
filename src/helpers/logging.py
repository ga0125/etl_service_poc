# ----------------------------------------------------------------------
# File: src/helpers/logging.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 26 jun 2021
# Brief: Config module for logging system.
# ----------------------------------------------------------------------
import time
import logging

from functools import wraps


# -----------------------------
# Set up wrapper logging
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] [%(funcName)s] [line %(lineno)d] - %(message)s ',
)


def timed(func: object) -> object:
    """This decorator prints the execution time for the decorated function.

    Args:
        func (object): Function to be logged.

    Returns:
        function: Return decorator.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.debug("{} ran in {}s".format(
            func.__name__, round(end - start, 2)))
        return result

    return wrapper
