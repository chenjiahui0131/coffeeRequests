#!/usr/bin/python3
from .pool import Pool
from fake_useragent import UserAgent


class UserAgentPool(Pool):

    def __init__(self):
        self.ua = UserAgent()

    def pick(self):
        return {'User-Agent': self.ua.random}

# vim: ts=4 sw=4 sts=4 expandtab
