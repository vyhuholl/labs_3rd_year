#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


def print_files():
    if len(sys.argv) <= 1:
        print('Usage:', sys.argv[0], '<dir path>')
        return

    dir_ = sys.argv[1]
    scandir = os.scandir(dir_)
    files = {}
    for i in scandir:
        if i.is_file() is True:
            name = i.name
            stat = i.stat()
            size = stat.st_size
            if size not in files:
                files[size] = [name]
            else:
                files[size].append(name)
    for size in reversed(sorted(files.keys())):
        for file in sorted(files[size]):
            print(file + '\t' + str(size))


if __name__ == "__main__":
    print_files()
