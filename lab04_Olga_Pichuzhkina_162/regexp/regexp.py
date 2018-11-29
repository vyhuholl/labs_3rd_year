#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from typing import List
from numbers import Number


def regexp_0(text: str, pattern: str) -> List[slice]:
    """
    Finds the occurrence and position of the substrings within a string

    >>> regexp_0("LingvoX SpaceX SpacoX", "oX")
    [slice(5, 7, None), slice(19, 21, None)]
    """
    pos = 0
    ans = []
    while True:
        reg = re.compile(pattern)
        result = reg.search(text, pos)
        if result is None:
            break
        ans.append(slice(result.start(), result.end(), None))
        pos = result.start()+1
    return ans


def regexp_1(text: str) -> str:
    """
    Converts camel case string to snake case string

    >>> regexp_1("QObject")
    'q_object'

    >>> regexp_1("KNeighborsClassifier")
    'k_neighbors_classifier'
    """
    uppercase_letters = re.findall(r'[A-Z]', text)
    lowercase_letters = re.split(r'[A-Z]', text)[1:]
    return '_'.join([start.lower() + end for start, end in
                     zip(uppercase_letters, lowercase_letters)])


def regexp_2(text: str, length: int) -> str:
    """
    Removes words from a string of length between 1 and a given number

    >>> regexp_2("Hello Cyril Kak dela bro", 3)
    'Hello Cyril dela'

    >>> regexp_2("Hello Cyril Kak dela bro", 4)
    'Hello Cyril'
    """
    regexp = re.compile(r'\W*\b\w{1,' + str(length) + r'}\b\W*')
    return regexp.sub('', text)


def regexp_3(text: str) -> str:
    """
    Removes the parenthesis area in a string

    >>> regexp_3("Polina (Ivan)")
    'Polina'

    >>> regexp_3("Mark (Station) (LingvoX)")
    'Mark'
    """
    return re.sub(r'\W*\(.*\)\W*', '', text)


def regexp_4(num: Number) -> bool:
    """
    Returns true whenever a decimal with a precision of 2

    >>> regexp_4(1.22)
    True
    >>> regexp_4(1.2)
    True
    >>> regexp_4(11)
    True
    >>> regexp_4(11.)
    True
    >>> regexp_4(11.333)
    False
    """
    match = re.match(r'\d*\.{0,1}\d{0,2}', str(num))
    if match:
        if len(match.group()) == len(str(num)):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
