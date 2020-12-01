import sys
from src.aoc.common import DataAnalyzer


def calc3(data, result=2020):
    length = len(data)
    for i in range(0, length-1):
        s = set()
        total = result - data[i]
        for j in range(i + 1, length):
            if (total - data[j]) in s:
                return i, j, data.index(total - data[j])
            s.add(data[j])
    
    return -1, -1, -1


def calc2(data, result=2020):
    length = len(data)
    for i in range(length):
        for j in range(i, length):
            if i != j and data[i] + data[j] == result:
                return i, j
    
    return -1, -1


def second():
    data = DataAnalyzer.ints("2020day1.txt")
    x, y, z = calc3(data)
    print("(1.2) 2020 {:d} {:d} {:d} => {:d}".format(x, y, z, data[x]*data[y]*data[z]))


def first():
    values = DataAnalyzer.ints("2020day1.txt")
    x, y = calc2(values)
    print("(1.1) 2020 {:d} {:d} => {:d}".format(x, y, values[x]*values[y]))


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
