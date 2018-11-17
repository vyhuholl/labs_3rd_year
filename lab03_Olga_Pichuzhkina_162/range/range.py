#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Sequence

class RangeIterator:

    def __init__(self, rangeobj):
        if not (isinstance(rangeobj, int) or isinstance(rangeobj, float)):
            raise TypeError
        self.stop = rangeobj
        if self.start == None:
            self.start = 0
        if self.step == None:
            self.step = 1

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration()
        else:
            self.current += self.step
        return self.current            

    def __iter__(self):
        return self


class Range(Sequence):

    def __init__(self, *args):
        self.start = None
        self.step = None
        for i in args:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError
        if len(args) == 1:
            RangeIterator.__init__(self, args[0])
        elif len(args) == 2:
            self.start = args[0]
            RangeIterator.__init__(self, args[1])
        elif len(args) == 3:
            self.start = args[0]
            RangeIterator.__init__(self, args[1])
            if args[2] == 0:
                raise ValueError
            else:
                self.step = args[2]
        else:
            raise TypeError

    def __eq__(self, other):
        return (self.start == other.start and self.stop == other.stop and self.step == other.step and isinstance(other, Range))

    def __iter__(self):
        return RangeIterator(self, self.stop)

    def __repr__(self):
        if self.step != 1:
            return f"range({self.start}, {self.stop}, {self.step})"
        else:
            return f"range({self.start}, {self.stop})"

    def __getitem__(self, key):
        if key > self.__len__():
            raise IndexError
        return self.start + key * self.step

    def __len__(self):
        return abs((self.stop - self.start) // self.step)

    def __contains__(self, value):
        if self.step > 0:
            return (value >= self.start and value <= self.stop and ((value - self.start) % self.step == 0))
        else:
            return (value >= self.stop and value <= self.start and ((value - self.stop) % self.step == 0))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
