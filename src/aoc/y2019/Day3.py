#!/usr/bin/python
from src.aoc.common import DataAnalyzer
import numpy as np
import sys

cursor = [0, 0]
crossings = list()
layout = []


def stepper(prefix, x, y):
    route = x * y
    for cross in crossings:
        total = 0
        for wire in layout:
            steps = 1
            for point in wire:
                if point == cross:
                    break
                else:
                    steps += 1

            total += steps

        route = min(route, total)

    return "({:s}) Step count is {:d}".format(prefix, route)


def manhattan(prefix, x, y):
    route = x * 100
    for cross in crossings:
        route = min(abs(cross[0] - x) + abs(cross[1] - y), route)

    return "({:s}) Shortest distance is {:d}".format(prefix, route)


def draw(name, x, y, size, spool, calculator):
    global layout, crossings, cursor
    layout = [[] for i in range(2)]
    crossings = list()
    cursor = [x, y]

    grid = np.zeros([size, size], dtype=int)
    grid[cursor[0], cursor[1]] = -1
    count = 1

    for crimps in spool:
        for crimp in crimps:
            solder = {
                'U':  up,
                'D':  down,
                'L':  left,
                'R':  right
            }

            solder[crimp[0]](grid, int(crimp[1:]), count)

        count += 1
        cursor = [x, y]

    print(calculator(name, x, y))
    # print(np.matrix(grid))


def etch(grid, x, y, etching):
    layout[etching-1].append([x, y])

    if grid[x][y] == 0 or grid[x][y] == etching:
        grid[x][y] = etching
    else:
        crossings.append([x, y])
        grid[x][y] = '-5'


def up(grid, distance, wire):
    for i in range(distance):
        cursor[0] -= 1
        etch(grid, cursor[0], cursor[1], wire)


def down(grid, distance, wire):
    for i in range(distance):
        cursor[0] += 1
        etch(grid, cursor[0], cursor[1], wire)


def left(grid, distance, wire):
    for i in range(distance):
        cursor[1] -= 1
        etch(grid, cursor[0], cursor[1], wire)


def right(grid, distance, wire):
    for i in range(distance):
        cursor[1] += 1
        etch(grid, cursor[0], cursor[1], wire)


def circuitry(puzzle, calculator):
    wiring = [['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']]
    draw("test", 8, 1, 11, wiring, calculator)

    # 610
    wiring = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], 
              ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
              ]
    draw("test", 300, 150, 500, wiring, calculator)

    # 410
    wiring = [['R98',  'U47',  'R26',  'D63',  'R33',  'U87',  'L62',  'D20',  'R33',  'U53',  'R51'],  
              ['U98',  'R91',  'D20',  'R16',  'D67',  'R40',  'U7',  'R15',  'U6',  'R7']
              ]
    draw("test", 200, 200, 500, wiring, calculator)

    wiring = DataAnalyzer.str_csv("2019day3.txt")
    draw(puzzle, 5000, 5000, 40000, wiring, calculator)


def solve(puzzle):
    if puzzle == '1':
        circuitry("3.1", manhattan)
    elif puzzle == '2':
        circuitry("3.2", stepper)
    else:
        circuitry("3.1", manhattan)
        circuitry("3.2", stepper)


if __name__ == '__main__':
    solve(sys.argv[1])
