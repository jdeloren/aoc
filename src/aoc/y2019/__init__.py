#!/usr/bin/python
__all__ = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7", "Day8", "Day9", "Day10"]

import sys
from aoc.y2019 import *


def solve(day, solver):
    executor = {
        '1': Day1.solve,
        '2': Day2.solve,
        '3': Day3.solve,
        '4': Day4.solve,
        '5': Day5.solve,
        '6': Day6.solve,
        '7': Day7.solve,
        '8': Day8.solve,
        '9': Day9.solve,
        '10': Day10.solve,
    }
    executor[day](solver)


if __name__ == '__main__':
    solve(sys.argv[1], sys.argv[2])
