#!/usr/bin/python3
import abc


class Pool(abc.ABC):

    @abc.abstractclassmethod
    def pick(self):
        pass

# vim: ts=4 sw=4 sts=4 expandtab
