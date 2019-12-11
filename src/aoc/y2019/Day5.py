from aoc import DataAnalyzer
from . import Computer


def second():
    inputs = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    print("(test-2-zeros-position)")
    Computer.opcoding(inputs.copy(), 0)
    Computer.opcoding(inputs.copy(), 1)
    Computer.opcoding(inputs.copy(), 2)
    inputs = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    print("(test-2-zeros-immediate)")
    Computer.opcoding(inputs.copy(), 0)
    Computer.opcoding(inputs.copy(), 1)
    Computer.opcoding(inputs.copy(), 2)

    inputs = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
              1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
              999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    print("(test-2-999/1000/1001)")
    Computer.opcoding(inputs.copy(), 0)
    Computer.opcoding(inputs.copy(), 3)
    Computer.opcoding(inputs.copy(), 8)
    Computer.opcoding(inputs.copy(), 9)

    values = DataAnalyzer.int_csv("2019day5.txt")[0]
    print("(5.2)")
    Computer.opcoding(values, 5)


def first():
    values = [3, 0, 4, 0, 99]
    Computer.opcoding(values, 55)
    print("(test)", end='')

    values = [1002, 4, 3, 4, 33]
    Computer.opcoding(values, 1)
    print("(test)", end='')

    values = [1101, 100, -1, 4, 0]
    Computer.opcoding(values, 1)
    print("(test)", end='')

    values = DataAnalyzer.int_csv("2019day5.txt")[0]
    print("(5.1)")
    Computer.opcoding(values, 1)


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
