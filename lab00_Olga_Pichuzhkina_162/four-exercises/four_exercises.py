#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def divisible(begin, end):
    """
    :param begin: int, positive integer
    :param end: int, positive integer
    :return: str, string of space separated integers

    Examples of usage:
    >>> divisible(1, 10)
    '7'
    >>> divisible(1, 17)
    '7 14'
    >>> len(divisible(100, 1000))
    407
    >>> divisible(29, 60)
    '42 49 56'
    >>> len(divisible(300, 3000).split())
    309
    >>> ns = [int(n) for n in divisible(300, 10000).split()]
    >>> seven_mask = [not bool(n % 7) for n in ns]
    >>> all(seven_mask)
    True
    >>> any(seven_mask)
    True
    >>> five_mask = [not bool(n % 5) for n in ns]
    >>> all(five_mask)
    False
    >>> any(five_mask)
    False
    >>> divisible(2, 5)
    ''
    >>> 1329 not in ns
    True
    """
    ans = []
    a = begin // 7
    b = end // 7
    for i in range(a, b + 1):
        if (7 * i) % 5 != 0 and 7 * i in range(begin, end + 1):
            ans.append(str(7 * i))
    return ' '.join(ans)


def register_count(string):
    """
    :param string: str, input string
    :return: dict, dict of lower and upper letter counts

    >>> register_count("Mama") == {'UPPER': 1, 'LOWER': 3}
    True
    >>> register_count("Your Name") == {'UPPER': 2, 'LOWER': 6}
    True
    >>> register_count("LingvoX!!!") == {'UPPER': 2, 'LOWER': 5}
    True
    >>> register_count("Trud, mir, mai! Zvahka!") == {'UPPER': 2, 'LOWER': 14}
    True
    >>> register_count("Coi ZIV!,,,,,") == {'UPPER': 4, 'LOWER': 2}
    True
    """
    ans = {'UPPER': 0, 'LOWER': 0}
    str_upper = string.upper()
    str_lower = string.lower()
    for i in range(len(string)):
        if string[i] != str_upper[i]:
            ans['LOWER'] += 1
        elif string[i] != str_lower[i]:
            ans['UPPER'] += 1
    return ans


def pairwise_diff(first, second):
    """

    :param first: str, first input string
    :param second: str, second input string
    :return: float, percentage of different letters

    >>> pairwise_diff('ABSD', 'ABCD')
    0.25
    >>> pairwise_diff('aBSD', 'ABCD')
    0.5
    >>> pairwise_diff('LingvX', 'SpaceX')
    0.83
    >>> pairwise_diff('LingvoX', 'SpaceX')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pairwise_diff('abc', 'ab')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> first = 'Salaman..'; second = 'Salaman.!'
    >>> round(1. / len(first), 2) == pairwise_diff(first, second)
    True
    >>> pairwise_diff(first + second, first + first)
    0.06
    >>> pairwise_diff(first * 3, second * 2 + first)
    0.07
    """
    assert len(first) == len(second)
    n = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            n += 1
    return(round(n / len(first), 2))


def run_robot():
    """
    Uses input() inside.
    :return: int, rounded euclidean distance from origin
    """
    movements = {'X': 0, 'Y': 0}
    while True:
        command = input()
        if command == '':
            break
        else:
            direction, n = command.split(' ')
            n = int(n)
            if direction == 'UP':
                movements['Y'] += n
            elif direction == 'DOWN':
                movements['Y'] -= n
            elif direction == 'RIGHT':
                movements['X'] += n
            elif direction == 'LEFT':
                movements['X'] -= n
            x = movements['X'] ** 2
            y = movements['Y'] ** 2
            distance = round(math.sqrt(x + y))
    return distance


if __name__ == "__main__":
    import doctest
    doctest.testmod()
