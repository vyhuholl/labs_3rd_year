#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy


def count_neighbours(state, x, y, n):
    neighbours = []
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            if i in range(len(state)) and j in range(len(state[0])):
                if [x, y] != [i, j]:
                    neighbours.append(state[i][j])
    return neighbours.count(n)


class Ocean:

    def __init__(self, init_state):
        self.state = init_state
        self.length = len(init_state[0])
        self.height = len(init_state)

    def __str__(self):
        ans = []
        for i in self.state:
            ans.append(' '.join([str(j) for j in i]))
        return '\n'.join(ans)

    def gen_next_quantum(self):
        next_state = deepcopy(self.state)
        for i in range(self.height):
            for j in range(self.length):
                if self.state[i][j] == 0:
                    if count_neighbours(self.state, i, j, 2) == 3:
                        next_state[i][j] = 2
                    elif count_neighbours(self.state, i, j, 3) == 3:
                        next_state[i][j] = 3
                elif self.state[i][j] == 2:
                    if count_neighbours(self.state, i, j, 2) not in [2, 3]:
                        next_state[i][j] = 0
                elif self.state[i][j] == 3:
                    if count_neighbours(self.state, i, j, 3) not in [2, 3]:
                        next_state[i][j] = 0
        self.state = next_state
        return self


if __name__ == '__main__':
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = [int(i) for i in sys.stdin.readline().split()]
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
