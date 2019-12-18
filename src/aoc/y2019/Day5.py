from aoc import DataAnalyzer
from . import Computer


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
