#!/usr/bin/python3
from coffeeRequests.proxy_pool import ProxyPool
from loguru import logger


def test_proxy_pool():
    proxy_pool = ProxyPool()
    logger.info(f'proxy number: {proxy_pool.size}')
    for i in range(10000):
        proxy = proxy_pool.pick()
        proxy_pool.fail(proxy)
    assert(proxy_pool.size == 1)
    assert(proxy_pool.pick().get_proxy() is None)
# vim: ts=4 sw=4 sts=4 expandtab
