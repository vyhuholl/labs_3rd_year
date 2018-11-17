#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ExtendedList(list):
    """
    >>> l = ExtendedList([1, 2, 3])
    >>> l.first
    >>> l.F = 4
    >>> l
    >>> l.size = 5
    >>> l.last = 100
    >>> l
    >>> l.size = 2
    >>> l
    >>> l.S = 0
    >>> l
    """

    aliases = {
        'first': 'F',
        'last': 'L',
        'size': 'S',
        'reversed': 'R',
        'F': 'first',
        'L': 'last',
        'S': 'size',
        'R': 'reversed'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = len(self)
        self.reversed = self[::-1]
        if len(self) != 0:
            self.F = self[0]
            self.L = self[-1]
            self.first = self[0]
            self.last = self[-1]

    def __setattr__(self, name, value):
        alias = self.aliases.get(name, name)
        object.__setattr__(self, name, value)
        object.__setattr__(self, alias, value)

    def __getattr__(self, name):
        if name == "aliases":
            raise AttributeError
        elif name in ["F", "L", "first", "last"] and len(self) == 0:
            raise IndexError('list index out of range')
        return object.__getattribute__(self, name)

    def __delattr__(self, name):
        alias = self.aliases.get(name, name)
        object.__delattr__(self, name)
        object.__delattr__(self, alias)

    def append(self, item):
        if len(self) == 0:
            self.first = item
        self.last = item
        self.reversed = [item] + self.reversed
        self.size += 1
        return ExtendedList(self + [item])

    def __delitem__(self, key):
        if (key == len(self) - 1 or key == -1) and len(self) > 1:
            self.last = self[-2]
        elif (key == -len(self) or key == 0) and len(self) > 1:
            self.first = self[1]
        elif len(self) == 1:
            self.__delattr__(first)
            self.__delattr__(last)
        self.reversed.remove(self[key])
        self.size -= 1
        self.remove(self[key])

    def __getitem__(self, key):
        if (key == 0 or key == -len(self)) and hasattr(self, "first"):
            return self.first
        elif (key == -1 or key == len(self) - 1) and hasattr(self, "last"):
            return self.last
        else:
            return list(self)[key]

    def __setitem__(self, key, value):
        if key == 0 or key == -len(self):
            self.first = value
        elif key == -1 or key == len(self) - 1:
            self.last = value
        if key >= 0:
            self.reversed = list(self[:key] + [value] + self[:key + 1])[::-1]
            return ExtendedList(self[:key] + [value] + self[:key + 1])
        else:
            self.reversed = list(self[:len(self) + key] +
                                 [value] + self[:len(self) + key + 1])[::-1]
            return ExtendedList(self[:len(self) + key]
                                + [value] + self[:len(self) + key + 1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
