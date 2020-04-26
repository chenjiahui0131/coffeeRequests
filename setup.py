#!/usr/local/bin/python3
from setuptools import setup, find_packages
import re
import os

name = "coffeeRequests"
HERE = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(HERE, fname)).read()


try:
    VERSION = re.search(
        r"__version__\s*=\s*['\"]([^'\"]+)['\"]",
        read(f"{name}/_version.py"),
    ).group(1)
except Exception:
    raise RuntimeError("Failed to parse version string")


setup(
    name=name,
    version=VERSION,
    author="chenjiahui",
    author_email="chenjiahui1991@163.com",
    description=("Tools for Economic Applications"),
    license="MIT Licence",
    packages=find_packages(include=(f"{name}*", )),
    package_data = {
        f"{name}": ["UA.json"]
    },
    install_requires=[
    ],
    include_package_data=False,
)

# vim: ts=4 sw=4 sts=4 expandtab
