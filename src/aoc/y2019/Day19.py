#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys


def second():
    def detection(x, y):
        if x > n and y > n:
            return True if radar[x-n][y-n:y].count(1) == n and [m[y-n] for m in radar[x-n:x]].count(1) == n else False
        else:
            return False

    values = DataAnalyzer.int_csv("2019day19.txt")[0]
    cpu = Computer.IntCode(values, extend=True, interrupt=False, auto=False, x=25000)
    done, i, j, size, n = False, 0, 0, 1700, 100
    radar = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            cpu.reset([i, j])
            cpu.start()
            radar[i][j] = cpu.output()[0]
            done = detection(i+1, j+1)
            if done:
                break

        if done:
            break

    print(f"(19.2) LOCATED: {done}, {n}x{n} block at {i-n+1},{j-n+1} :: ship math = {(i-n+1)*10000 + j-n+1}")


def first():
    values = DataAnalyzer.int_csv("2019day19.txt")[0]
    count = 0
    cpu = Computer.IntCode(values, extend=True, interrupt=False, auto=False)

    for i in range(50):
        for j in range(50):
            cpu.reset([i, j])
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
