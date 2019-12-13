from aoc import DataAnalyzer
from . import Computer


def second():
    values = DataAnalyzer.int_csv("2019day9.txt")[0]
    print(f"(9.2)")
    Computer.opcoding(values.copy(), 2)


def first():
    values = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    print(f"Running input{values}")
    Computer.opcodes(values, -1, -1)

    values = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    print(f"Running input{values}")
    Computer.opcodes(values, -1, -1)

    values = DataAnalyzer.int_csv("2019day9.txt")[0]
    print(f"(9.1)")
    Computer.opcoding(values.copy(), 1)


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
