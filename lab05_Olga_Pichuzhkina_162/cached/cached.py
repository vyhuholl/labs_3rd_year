#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def cached(func):
    """
    >>> @cached
    ... def add(a, b):
    ...     print(a, b)
    ...     return a + b
    ...
    >>> add(1, 2)
    1 2
    3
    >>> add(1, 2)
    3
    >>> add(2, 2)
    2 2
    4
    >>> add(2, 2)
    4
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*fargs, **fkwargs):
        args = fargs + tuple(sorted(fkwargs.items()))
        if args not in cache:
            cache[args] = func(*fargs, **fkwargs)
        return cache[args]
    return wrapper


if __name__ == '__main__':
    import doctest
    doctest.testmod()
