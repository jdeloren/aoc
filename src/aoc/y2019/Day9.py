#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys


def second():
    values = DataAnalyzer.int_csv("2019day9.txt")[0]
    computer = Computer.IntCode(values, [2], extend=True, auto=True)
    print(f"(9.2) {computer.output()[0]}")


def first():
    values = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    computer = Computer.IntCode(values, extend=True, auto=True)
    print(f"(test) {computer.output()}")

    values = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    computer = Computer.IntCode(values, extend=True, auto=True)
    print(f"(test) {computer.output()[0]}")

    values = DataAnalyzer.int_csv("2019day9.txt")[0]
    computer = Computer.IntCode(values, [1], extend=True, auto=True)
    print(f"(9.1) {computer.output()[0]}")


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
