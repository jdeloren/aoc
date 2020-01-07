#!/usr/bin/python
from src.aoc.common import DataAnalyzer
from src.aoc.y2019 import Computer
import sys
import itertools


def amplifier(values, phase, thrusters, signal, amplify):
    complete = 1
    active = None
    inputs = [signal]
    output = [0 for _ in range(len(phase))]

    computers = [Computer.IntCode(values.copy(), phase[i], interrupt=amplify) for i in range(len(phase))]

    while complete <= len(phase):
        active = 0 if active is None else thrusters[active]
        cpu = computers[active]
        # cpu.debug(True)

        if not cpu.done:
            if len(inputs) > 0:
                computers[active].inputs(inputs.pop(0))

            cpu.start()
            data = cpu.output()

            if len(data) > 0:
                output[active] = data[0]
                inputs.append(data[0])

            if cpu.done:
                complete += 1

    return output


def sequencer(values, thrusters, finder='', amplify=False):
    signal = 0
    max_sequence = [0, 0, 0, 0, 0]
    max_signal = 0

    for numbers in itertools.permutations(finder):
        sequence = [int(x) for x in numbers]
        outs = amplifier(values, [[s] for s in sequence], thrusters, signal, amplify)

        if outs[-1] > max_signal:
            max_sequence = sequence
            max_signal = outs[-1]

    print(f"Signals: {max_sequence} -> {max_signal}!")


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


if __name__ == '__main__':
    solve(sys.argv[1])
