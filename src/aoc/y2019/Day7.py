from aoc import DataAnalyzer
from . import Computer
import itertools


def sequencer(values, thrusters, finder='', amplify=False):
    signal = 0
    sequence = [0, 0, 0, 0, 0]

    for numbers in itertools.permutations(finder):
        sequencing = [int(x) for x in numbers]
        # if amplify:
        #     print("Sequence: ({:s})".format(' '.join(map(str, sequencing))))
        outs = Computer.amplifier(values, sequencing, thrusters, 0, amplify)

        if outs[len(outs)-1] > signal:
            sequence = sequencing
            signal = outs[len(outs)-1]
            # print("New max: ({:s}) -> {:d}".format(' '.join(map(str, sequence)), signal))

    print("Signals: ", end='')
    print(sequence, end='')
    print(" -> ", end='')
    print(signal, end='')
    print("!")


def second():
    configuration = {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 0
    }

    inputs = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 
              27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
    sequencer(inputs, configuration, '56789', True)

    values = DataAnalyzer.int_csv("2019day7.txt")[0]
    print("(7.2)", end='')
    sequencer(values, configuration, '56789', True)


def first():
    configuration = {
        0: 1,
        1: 2,
        2: 3,
        3: 4
    }

    inputs = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    sequencer(inputs, configuration, '01234')

    inputs = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101,
              5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
    sequencer(inputs, configuration, '01234')
    inputs = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002,
              33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
    sequencer(inputs, configuration, '01234')

    print("(7.1) ", end='')
    inputs = DataAnalyzer.int_csv("2019day7.txt")[0]
    sequencer(inputs, configuration, '01234')


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
