#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy


class Transaction:

    def __init__(self, storage):
        self.storage = storage

    def __enter__(self):
        self.old_data = copy(self.storage._data)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            return self
        elif exc_value is None:
            exc_value = exc_type()
        self.storage._data = self.old_data
        raise(exc_type(exc_value))

    def __setitem__(self, key, value):
        self.storage._data[key] = value

    def __getitem__(self, key):
        return self.storage._data[key]

    def __delitem__(self, key):
        del self.storage._data[key]


class Storage:
    """

    >>> try:
    ...     s = Storage()
    ...     with s.edit() as e:
    ...         e['a'] = 1
    ...         1/0
    ...     print(s['a'])
    ... except ZeroDivisionError:
    ...     print(s['a'])
    Traceback (most recent call last):
    ...
    KeyError: 'a'
    """

    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def edit(self):
        return Transaction(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
