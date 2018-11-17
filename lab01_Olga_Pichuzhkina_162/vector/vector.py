#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


class Vector(list):
    """
    Class Vector is n-dimensional geometry vector.

    Examples of usage:

    >>> a = Vector([1, 2, 3, 4])
    >>> b = Vector([0, 1, -1, -4])
    >>> a
    Vector([1, 2, 3, 4])
    >>> a + b
    Vector([1, 3, 2, 0])
    >>> a - b
    Vector([1, 1, 4, 8])
    >>> print(a * b)
    Vector([0, 2, -3, -16])
    >>> print(b / a)
    Vector([0.0, 0.5, -0.3333333333333333, -1.0])
    >>> a == Vector([1, 2, 3, 4])
    True
    >>> a.append(144)
    >>> print(a)
    Vector([1, 2, 3, 4, 144])
    >>> len(a)
    5
    >>> a.ndim() == 5
    True
    >>> a[1] == 2
    True
    >>> a[-1] = 5
    >>> a[-1]
    5
    >>> a.clear()
    >>> not a
    True
    >>> b.reverse()
    >>> b
    Vector([-4, -1, 1, 0])
    >>> abs(b) == sqrt(16 + 1 + 1 + 0)
    True
    >>> b.argmin()
    0
    >>> b[b.argmin()] == -4
    True
    >>> b.argmax()
    2
    >>> b[b.argmax()] == 1
    True
    >>> [i for i in b] == [-4, -1, 1, 0]
    True
    """
    def __repr__(self):
        ans = 'Vector(['
        for i in self:
            ans += str(i) + ', '
        ans = ans.rstrip(', ')
        ans += '])'
        return ans

    def ndim(self):
        return len(self)

    def clear(self):
        del self

    def argmin(self):
        return min(self)

    def argmax(self):
        return max(self)

    def __add__(self, other):
        return Vector([i + j for i, j in zip(self, other)])

    def __sub__(self, other):
        return Vector([i - j for i, j in zip(self, other)])

    def __mul__(self, other):
        return Vector([i * j for i, j in zip(self, other)])

    def __truediv__(self, other):
        return Vector([i / j for i, j in zip(self, other)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
