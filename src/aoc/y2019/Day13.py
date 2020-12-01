#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys


def play(values, debug=False):
    ball = paddle = None
    point = 0

    def inputter():
        return (ball > paddle) - (ball < paddle)

    values[0] = 2
    computer = Computer.IntCode(values, input_func=inputter, extend=True, interrupt=True)
    computer.debug(debug)

    while not computer.done:
        computer.start()
        computer.start()
        computer.start()
        blocks = computer.output(3)

        if not computer.done:
            paddle = blocks[0] if blocks[2] == 3 else paddle
            ball = blocks[0] if blocks[2] == 4 else ball
            point = blocks[2] if (blocks[0], blocks[1]) == (-1, 0) else point

    return point


def second():
    values = DataAnalyzer.int_csv("2019day13.txt")[0]
    codes = play(values.copy())
    print(f"(13.2) Final score: {codes}")


def first():
    values = DataAnalyzer.int_csv("2019day13.txt")[0]
    computer = Computer.IntCode(values, extend=True, auto=True)

    count = 0
    output = computer.output()
    for i in range(0, len(output), 3):
        count += 1 if output[i+2] == 2 else 0

    print(f"(13.1) Block tile count: {count}")


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
