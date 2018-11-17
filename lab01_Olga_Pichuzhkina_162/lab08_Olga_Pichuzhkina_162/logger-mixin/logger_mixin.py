#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class LoggerMixin(object):

    """Logs all method calls in the class."""
    raise NotImplementedError


class Test(LoggerMixin):
    """
    >>> t = Test()
    >>> t.test(1, 2, c=22)
    25
    >>> t.test(17, 2, c=12)
    31
    >>> print(t)
    Called test(). args: (1, 2), kwargs: {'c': 22}, return: 25
    Called test(). args: (17, 2), kwargs: {'c': 12}, return: 31
    """
    def test(self, a, b, c=None):
        return a + b + c


if __name__ == '__main__':
    import doctest
    doctest.testmod()
