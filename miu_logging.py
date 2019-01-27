"""Logging functions for MIU."""

import logging
import logging.handlers as handlers


def get_logger(filename):
    """
    Get a logger for debugging.

    :param filename: The file to store logs.
    :return: A Python logger.
    """
    logger = logging.getLogger('mui-logger')
    handler = handlers.RotatingFileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
