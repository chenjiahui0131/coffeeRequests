#!/usr/bin/python3
from loguru import logger

from coffeeRequests.user_agent_pool import UserAgentPool


def test_user_agent_pool():
    logger.info(f'Begin - test_user_agent_pool')
    ua_pool = UserAgentPool()
    for i in range(10000):
        assert(len(ua_pool.pick()) > 0)
    logger.info(f'End - test_user_agent_pool')
# vim: ts=4 sw=4 sts=4 expandtab
