#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys


def second():
    values = DataAnalyzer.int_csv("2019day19.txt")[0]
    cpu = Computer.IntCode(values, extend=True, auto=True)


def first():
    values = DataAnalyzer.int_csv("2019day19.txt")[0]
    count = 0
    for i in range(50):
        for j in range(50):
            cpu = Computer.IntCode(values.copy(), [i, j], extend=True, interrupt=False, auto=True)
            cpu.start()
            count += 1 if cpu.output()[0] == 1 else 0
    print(f"(19.1) affected points: {count}")


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
