#!/usr/bin/python3
import requests
from loguru import logger

from .proxy_pool import ProxyPool, Proxy
from .user_agent_pool import UserAgentPool

_proxy_pool = ProxyPool()
_user_agent_pool = UserAgentPool()


def get(url, headers=None, no_proxy=False, **kwargs):
    try:
        headers = headers or _user_agent_pool.pick()
        proxies = Proxy(None, None, None, 100) if no_proxy else _proxy_pool.pick()
        response = requests.get(
            url, headers=headers, proxies=proxies.get_proxy(),
            allow_redirects=False, **kwargs
        )
    except Exception:
        logger.info(f'{proxies} is not available')
        _proxy_pool.fail(proxies)
        raise ConnectionError
    else:
        _proxy_pool.success(proxies)
    return response

# vim: ts=4 sw=4 sts=4 expandtab
