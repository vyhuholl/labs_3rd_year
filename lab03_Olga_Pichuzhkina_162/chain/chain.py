#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def lazy_chain(iterable):
    try:
        for element in iterable:
            if element != iterable:
                yield from lazy_chain(element)
            else:
                yield element
    except TypeError:
        yield iterable


def chain(*iterables):
    for it in iterables:
        yield from lazy_chain(it)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
