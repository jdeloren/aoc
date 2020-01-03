#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys


def find_alignment(scaffolding):
    def is_mark(x, y):
        return 1 if ((x, y) in scaffolding and scaffolding[(x, y)] == '#') else 0

    intersections = []
    for i in scaffolding:
        if is_mark(i[0], i[1]) == 1:
            marks = is_mark(i[0]-1, i[1])
            marks += is_mark(i[0]+1, i[1])
            marks += is_mark(i[0], i[1]-1)
            marks += is_mark(i[0], i[1]+1)

            if marks >= 3:
                intersections.append(i)

    sigma = 0
    for intersect in intersections:
        sigma += intersect[0] * intersect[1]

    print(f"(17.1) Intersections: {len(intersections)}, sum: {sigma}")


def generate(diagram, debug):
    x, y = 0, 0
    grid = {}
    chars = [10, 35, 46, 60, 62, 94, 118]
    path = 0

    for point in diagram:
        if debug:
            print({35: '#', 46: '.', 10: '\n', 94: '^'}[point], end='')

        if point == 10:
            x = 0
            y += 1
        elif point in chars:
            grid[(x, y)] = chr(point)
            x += 1

            if point == 35:
                path += 1

    return grid


def get_scaffolding(values, debug=False):
    computer = Computer.IntCode(values, extend=True, auto=True)
    while not computer.done:
        computer.start()

    return computer, generate(computer.output(), debug)


def ascii_instructions(string):
    return list(map(ord, list(string)))


def second():
    values = DataAnalyzer.int_csv("2019day17.txt")[0]
    values[0] = 2
    listing = ascii_instructions('B,E,B,E,C,D,A,C,D,A,C,D,A,C,B,E\n'
                                 'L,10\n'
                                 'L,10,L,8,R,8\n'
                                 'R,6,R,8,R,8\n'
                                 'R,6,R,6,L,8\n'
                                 'L,6,R,8\n'
                                 'n\n')

    cpu = Computer.IntCode(values, listing, extend=True)

    print(f"Dust collection start, program: {listing}")
    while not cpu.done:
        cpu.inputs(listing.pop(0))
        cpu.start()

        #if cpu.done:
        print(f"OUTPUT: {cpu.output(1)}")

    print(f"Dust collection complete")


def first():
    values = DataAnalyzer.int_csv("2019day17.txt")[0]
    cpu, scaffolding = get_scaffolding(values, True)
    find_alignment(scaffolding)


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
