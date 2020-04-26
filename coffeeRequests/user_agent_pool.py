#!/usr/bin/python3
import os
from fake_useragent import UserAgent

from .pool import Pool


class UserAgentPool(Pool):

    def __init__(self):
        json_path = os.path.dirname(os.path.abspath(__file__))
        self.ua = UserAgent(path=f'{json_path}/UA.json')

    def pick(self):
        return {'User-Agent': self.ua.random}

# vim: ts=4 sw=4 sts=4 expandtab
