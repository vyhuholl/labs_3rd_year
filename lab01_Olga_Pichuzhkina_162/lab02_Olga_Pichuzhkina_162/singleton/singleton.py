#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Singleton:
    instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# from native python data types, None is a singleton, since there
# is only one instance of it, True and False are singletons, which
# is prowed by the following code:
# >>> a = True
# >>> b = True
# >>> id(a) == id(b)
# True
