#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def minimum(*args, **kwargs):
    """
    The same as built-in min (exclude default parameter).
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.

    >>> minimum(1, 2, 3) == min(1, 2, 3)
    True
    >>> minimum([1, 2, 3]) == min([1, 2, 3])
    True
    """
    if len(args) == 1:
        it = args[0]
    else:
        it = args
    if 'key' in kwargs:
        for i in it:
            if 'min_item' not in locals():
                min_item = i
            elif kwargs['key'](i) < kwargs['key'](min_item):
                min_item = i
    else:
        for i in it:
            if 'min_item' not in locals():
                min_item = i
            elif i < min_item:
                min_item = i
    return min_item


def maximum(*args, **kwargs):
    """
    The same as built-in max (exclude default parameter).
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.

    >>> maximum(1, 2, 3) == max(1, 2, 3)
    True
    >>> maximum([1, 2, 3]) == max([1, 2, 3])
    True
    """
    if len(args) == 1:
        it = args[0]
    else:
        it = args
    if 'key' in kwargs:
        for i in it:
            if 'max_item' not in locals():
                max_item = i
            elif kwargs['key'](i) > kwargs['key'](max_item):
                max_item = i
    else:
        for i in it:
            if 'max_item' not in locals():
                max_item = i
            elif i > max_item:
                max_item = i
    return max_item


if __name__ == "__main__":
    import doctest
    doctest.testmod()
