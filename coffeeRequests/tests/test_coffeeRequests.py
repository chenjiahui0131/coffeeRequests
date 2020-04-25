#!/usr/bin/python3
from coffeeRequests import coffeeRequests as requests


def test_coffeeRequests():
    for i in range(1000):
        try:
            response = requests.get('http://www.baidu.com', timeout=0.1)
            print(len(response.text))
        except ConnectionError:
            pass
# vim: ts=4 sw=4 sts=4 expandtab
