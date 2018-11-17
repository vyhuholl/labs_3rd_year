#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy


class Buckets:

    def __init__(self, length=0, default=None):
        # set default 'length' and 'default' so it passes b = Buckets() test
        self.default = copy(default)
        # copy passes assertNotEqual(id(default), id(b.default)) test
        self.buckets = [copy(default)] * length
        # copy passes assertFalse(b.find(3, [3])) test
        # after default.append([3]) and b.clear(3) were made

    def add(self, index, element):
        self.buckets[index].append(copy(element))
        # copy passes assertTrue(b.find(0, item))
        # after item was added to bucket and then changed

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = self.default


if __name__ == "__main__":
    import doctest
    doctest.testmod()
