#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys


def second():
    values = DataAnalyzer.int_csv("2019day5.txt")[0]
    computer = Computer.IntCode(values, [5], auto=True)
    print(f"(5.2) {computer.output()[0]}")


def first():
    values = DataAnalyzer.int_csv("2019day5.txt")[0]
    computer = Computer.IntCode(values, [1], auto=True)
    print(f"(5.1) {computer.output()}")


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
