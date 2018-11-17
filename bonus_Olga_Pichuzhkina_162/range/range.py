#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable, Sequence

class RangeIterator:

    def __init__(self, rangeobj):
        self.rangeobj = rangeobj
        self.position = rangeobj.start

    def __next__(self):
        value = self.position
        self.position += self.rangeobj.step
        if value < self.rangeobj.stop and self.rangeobj.step > 0:
            return value
        elif value > self.rangeobj.stop and self.rangeobj.step < 0:
            return value
        else:
            raise StopIteration()

    def __iter__(self):
        return self


class Range(Sequence, Iterable):

    def __init__(self, *args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"'{arg.__class__.__name__}'"
                                f" object cannot be interpreted as an integer")
        if len(args) not in range(1, 4):
            raise TypeError(f"range expected at most 3 arguments,"
                            f" got {len(args)}")
        elif len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = *args, 1
        elif len(args) == 3:
            start, stop, step = args
        if step == 0:
            raise ValueError("range() arg 3 must not be zero")

        self.start, self.stop, self.step = start, stop, step

    def count(self, value):
        item = self.start
        ans = 0
        if self.step > 0:
            while item < self.stop:
                if item == value:
                    ans += 1
                item += self.step
        else:
            while item > self.stop:
                if item == value:
                    ans += 1
                item += self.step
        return ans

    def index(self, value):
        i = 0
        while i != len(self):
            if (self.start + i * self.step) == value:
                return i
            i += 1
        if isinstance(value, int):
            raise ValueError(f"{value} is not in range")
        else:
            raise ValueError("sequence.index(x): x not in sequence")

    def __iter__(self):
        return RangeIterator(self)
    
    def __eq__(self, other):
        return isinstance(other, Range) and\
               self.start == other.start and\
               self.stop == other.stop and\
               self.step == other.step

    def __repr__(self):
        if self.step == 1:
            return f"range({self.start}, {self.stop})"
        return f"range({self.start}, {self.stop}, {self.step})"

    def __getitem__(self, key):
        if not isinstance(key, slice):
            pos = self.start + key * self.step
            if self.step > 0 and pos < self.stop:
                return pos
            elif self.step < 0 and pos > self.stop:
                return pos
            else:
                raise IndexError("range object index out of range")
        else:   
            if key.step == None:
                step = self.step
            else:
                step = key.step * self.step
            if step > 0:
                if key.start != None:
                    start = key.start
                else:
                    start = self.start
                if key.stop != None:
                    stop = key.stop
                else:
                    stop = self.stop
            else:
                if key.start != None:
                    start = key.start
                else:
                    start = self.start
                if key.stop != None:
                    stop = key.stop
                else:
                    stop = self.stop
            return Range(start, stop, step)

    def __len__(self):
        len_ = (self.stop - self.start) // self.step +\
               bool((self.stop - self.start) % self.step)
        if len_ < 0:
            return 0
        return len_

    def __contains__(self, value):
        if not (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            return False
        if isinstance(value, complex):
            value = value.real
        diff = value - self.start
        q, r = divmod(diff, self.step)
        if r == 0 and 0 <= q < len(self):
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
