#!/usr/bin/python3
from loguru import logger

from coffeeRequests import coffeeRequests as requests


def test_coffeeRequests():
    logger.info(f'Begin - test_coffeeRequests')
    for i in range(1000):
        try:
            response = requests.get('http://www.baidu.com', timeout=0.2)
            logger.info(f'Received {len(response.text)}')
        except ConnectionError:
            pass
    logger.info(f'End - test_coffeeRequests')
# vim: ts=4 sw=4 sts=4 expandtab
