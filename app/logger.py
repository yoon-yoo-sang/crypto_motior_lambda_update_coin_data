import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)
