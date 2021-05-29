import logging
import sys

__APP_LOGGER_NAME = 'MyApp'


def setup_app_level_logger(logger_name=__APP_LOGGER_NAME, file_name=None):
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    sh = logging.StreamHandler(sys.stdout)

    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)

    if file_name:
        fh = logging.FileHandler(file_name)

        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def get_logger(module_name):
    return logging.getLogger(__APP_LOGGER_NAME).getChild(module_name)


__all = ['setup_app_level_logger', 'get_logger']
