import sys
from src.aoc.common import DataAnalyzer

def passwd(data):
    for str in data:
        words = str.split()
    
        bounds = words[0].split('-')
        yield [int(bounds[0]), int(bounds[1]), words[1][0], words[2]]


def bound_check(data):
    valid = 0
    instructions = passwd(data)

    for i in instructions:
        match = i[3].count(i[2])
        if (match >= i[0] and match <= i[1]):
            valid += 1

    return valid


def index_check(data):
    valid = 0
    instructions = passwd(data)

    for i in instructions:
        if (i[3][i[0]-1] == i[2]) != (i[3][i[1]-1] == i[2]):
            valid += 1

    return valid


def second():
    data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]
    print("(2.2.0) test valid passwords is {:d}".format(index_check(data)))

    data = DataAnalyzer.load("2020day2.txt")
    print("(2.2) test valid passwords is {:d}".format(index_check(data)))


def first():
    data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]

    print("(2.1.0) test valid passwords is {:d}".format(bound_check(data)))

    data = DataAnalyzer.load("2020day2.txt")
    print("(2.2) valid passwords is {:}".format(bound_check(data)))


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
