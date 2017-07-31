import logging

logging.basicConfig(level='DEBUG')


def getLogger(name):
    return logging.getLogger(name)
