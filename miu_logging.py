"""Logging functions for MIU."""

import logging
import logging.handlers as handlers


def get_logger(filename: str,
               num_bytes: int = 10000,
               num_files: int = 2
               ) -> logging.Logger:
    """
    Get a logger for debugging.

    :param filename: The file to store logs.
    :num_files: The number of files to rotate between.
    :return: A Python logger.
    """
    logger = logging.getLogger('mui-logger')
    handler = handlers.RotatingFileHandler(filename,
                                           maxBytes=num_bytes,
                                           backupCount=num_files)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
