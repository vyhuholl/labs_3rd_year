#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A:
    _init = 0

    def __init__(self, a, **kwargs):
        A._init += 1
        self.a = a
        for key, value in kwargs.items():
            setattr(self, key, value)


class B(A):
    _init = 0

    def __init__(self, b1, b2, a, **kwargs):
        B._init += 1
        super().__init__(b1=b1, b2=b2, a=a)
        self.b1 = b1
        self.b2 = b2
        for key, value in kwargs.items():
            setattr(self, key, value)


class C(A):
    _init = 0

    def __init__(self, c1, c2, a, **kwargs):
        C._init += 1
        super().__init__(c1=c1, c2=c2, a=a)
        self.c1 = c1
        self.c2 = c2
        for key, value in kwargs.items():
            setattr(self, key, value)


class D(B, C):
    _init = 0

    def __init__(self, d1, d2, c1, c2, b1, b2, a, **kwargs):
        B._init += 1
        C._init += 1
        super().__init__(
            a=a, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)
        self.d1 = d1
        self.d2 = d2


def main():
    pass


if __name__ == "__main__":
    main()
