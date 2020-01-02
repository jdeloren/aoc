#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import numpy as np
import sys


def draw(values, size=100, init=1):
    p = [int(size/2), int(size/2)]
    direction = 0
    grid = np.zeros([size, size], dtype=int)    # storing 1=black, 2=white
    grid[p[0], p[1]] = init

    compass = {-1: 3, 0: 0, 1: 1, 2: 2, 3: 3, 4: 0}

    def step(x, y):
        if x == 0:
            p[0] += 1 if y == 1 else -1
        elif x == 1:
            p[1] += 1 if y == 1 else -1
        elif x == 2:
            p[0] += -1 if y == 1 else 1
        elif x == 3:
            p[1] += -1 if y == 1 else 1

    def inputter():
        return 1 if grid[p[0]][p[1]] == 2 else 0

    computer = Computer.IntCode(values, [2], input_func=inputter, extend=True, interrupt=True)

    while not computer.done:
        computer.start()
        computer.start()
        data = computer.output(2)

        if not computer.done:
            grid[p[0], p[1]] = data[0] + 1
            step(direction, data[1])
            direction = compass[direction + (-1 if data[1] == 0 else 1)]

    return grid


def second():
    values = DataAnalyzer.int_csv("2019day11.txt")[0]
    grid = draw(values.copy(), 90, 2)

    print("(11.2) MESSAGE INCOMING:")

    for i in range(len(grid)):
        printed = False
        for j in range(len(grid)):
            if grid[i][j] > 0:
                printed = True
                print(f"{' ' if grid[i][j] == 1 else '*'}", end='')
        if printed:
            print()


def first():
    values = DataAnalyzer.int_csv("2019day11.txt")[0]
    grid = draw(values.copy())
    unique, counts = np.unique(grid, return_counts=True)
    zipped = dict(zip(unique, counts))
    print(f"(11.1) drawing: {zipped}, painted: {zipped[1] + zipped[2]}")


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()


if __name__ == '__main__':
    solve(sys.argv[1])
