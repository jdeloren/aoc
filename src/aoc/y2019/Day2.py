from aoc import DataAnalyzer
from . import Computer


def second():
    original = DataAnalyzer.int_csv("2019day2.txt")[0]
    target = 19690720
    done = False

    for i in range(0, 100):
        for j in range(0, 100):
            values = original.copy()
            Computer.opcodes(values, i, j)
            if values[0] == target:
                # 7912
                print("(2.2) Target matched with {:d}, {:d} to output of {:d}".format(i, j, (100 * i + j)))
                done = True
                break

        if done:
            break

    if not done:
        print("Target not matched!!")


def first():
    values = DataAnalyzer.int_csv("2019day2.txt")[0]
    Computer.opcodes(values, 12, 2)

    print("(2.1) Left position for gravity program: {:d}".format(values[0]))


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
