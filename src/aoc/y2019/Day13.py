from aoc import DataAnalyzer
from . import Computer


def play(values, debug=False):
    ball = paddle = None
    done = False
    point = base = index = 0

    def inputter():
        return (ball > paddle) - (ball < paddle)

    values[0] = 2
    while not done:
        a, index, base, done = Computer.opcodes(values, index, base, inputter, True, debug)
        b, index, base, done = Computer.opcodes(values, index, base, inputter, True, debug)
        c, index, base, done = Computer.opcodes(values, index, base, inputter, True, debug)

        if not done:
            paddle = a[0] if c[0] == 3 else paddle
            ball = a[0] if c[0] == 4 else ball
            point = c[0] if (a[0], b[0]) == (-1, 0) else point

    return point


def second():
    values = DataAnalyzer.int_csv("2019day13.txt")[0]
    print("(13.2)")
    codes = play(values.copy())
    print(codes)


def first():
    values = DataAnalyzer.int_csv("2019day13.txt")[0]
    print("(13.1)")
    codes = Computer.opcoding(values.copy(), None, False)[0]

    count = 0
    for i in range(0, len(codes), 3):
        count += 1 if codes[i+2] == 2 else 0

    print(f"Block tile count: {count}")


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
