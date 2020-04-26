#!/usr/bin/python3
from loguru import logger

from coffeeRequests.proxy_pool import ProxyPool


def test_proxy_pool():
    logger.info(f'Begin - test_proxy_pool')
    proxy_pool = ProxyPool()
    logger.info(f'proxy number: {proxy_pool.size}')
    for i in range(500):
        proxy = proxy_pool.pick()
        proxy_pool.fail(proxy)
    assert(proxy_pool.size == 1)
    assert(proxy_pool.pick().get_proxy() is None)
    logger.info(f'End - test_proxy_pool')
# vim: ts=4 sw=4 sts=4 expandtab
