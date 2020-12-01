import math
from src.aoc.common import DataAnalyzer


def calc(num):
    return int(math.floor(int(num) / 3) - 2)


def second():
    values = DataAnalyzer.load("2019day1.txt")
    total = 0
    for num in values:
        running = int(math.floor(int(num) / 3) - 2)
        while running > 0:
            total += running
            running = int(math.floor(int(running) / 3) - 2)

    print("(1.2) total fuel: {:d}".format(total))


def first():
    values = DataAnalyzer.load("2019day1.txt")
    total = 0

    for num in [12, 14, 1969, 100756]:
        print("(test): {:d}".format(calc(num)))

    for num in values:
        total += calc(num)

    print("(1.1) total fuel: {:d}".format(total))


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
