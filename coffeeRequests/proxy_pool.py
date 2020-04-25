#!/usr/bin/python3
from dataclasses import dataclass
import random
import requests
import json
from loguru import logger

from .pool import Pool

proxy_url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'


@dataclass
class Proxy:
    host: str = '127.0.0.1'
    port: int = 8080
    ptype: str = 'http'
    life: int = 100

    def get_proxy(self):
        if self.host is None:
            return None
        proxy = {
            self.ptype: f'{self.ptype}://{self.host}:{self.port}'
        }
        return proxy

    @property
    def key(self):
        if self.host is None:
            return None
        return f'{self.ptype}://{self.host}:{self.port}'


class ProxyPool(Pool):

    def __init__(self, num_retry=1, num_ratio=3):
        response = requests.get(proxy_url)
        item_list = response.text.strip().split('\n')
        proxy_list = []
        for item in item_list:
            proxy_js = json.loads(item)
            proxy_list.append(
                Proxy(proxy_js['host'], proxy_js['port'], proxy_js['type'], num_retry)
            )
        self.proxies = {None: Proxy(None, None, None, 100)}
        for proxy in proxy_list:
            self.proxies[proxy.key] = proxy
        self.num_retry = num_retry
        self.num_ratio = num_ratio

    @property
    def size(self):
        return len(self.proxies)

    def pick(self):
        return random.choice(list(self.proxies.items()))[1]

    def fail(self, proxy: Proxy):
        if proxy.key is None:
            return
        try:
            key = proxy.key
            if key in self.proxies.keys():
                if self.proxies[key].life == 1:
                    self.proxies.pop(key)
                    logger.info(f'Current proxy pool size: {self.size}')
                else:
                    self.proxies[key].life -= 1
        except Exception:
            logger.exception(f'{key} is not exists')

    def success(self, proxy: Proxy):
        if proxy.key is None:
            return
        try:
            key = proxy.key
            if key in self.proxies.keys():
                self.proxies[key].life = self.num_retry * self.num_ratio
        except Exception:
            logger.exception(f'{key} is not exists')

# vim: ts=4 sw=4 sts=4 expandtab
