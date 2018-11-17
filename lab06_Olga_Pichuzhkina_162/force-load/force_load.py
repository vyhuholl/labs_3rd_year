#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import traceback
import sys
import re


def force_load(module_name: str)-> dict:
    """
    >>> isinstance(force_load("bad_foo"), dict)
    True
    >>> len(force_load("bad_foo"))
    1
    >>> force_load("bad_foo")["foo"]("foo")
    'foo foo'
    """
    returned_dict = {}
    clean = False
    with open(module_name + '.py', 'r') as module:
        lines = module.readlines()
        while clean == False:
            try:
                exec(''.join(lines), globals(), returned_dict)
                clean = True
            except SyntaxError as err:
                line_number = err.lineno
                del lines[line_number - 1]
            except Exception as err:
                cl, exc, tb = sys.exc_info()
                line_number = traceback.extract_tb(tb)[-1][1]
                del lines[line_number - 1]
    return returned_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod()
