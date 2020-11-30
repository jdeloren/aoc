#!/usr/bin/python
from src.aoc.common import DataAnalyzer
import sys


def fft(sequence, pattern, digits, phases):
    def sequencer(sequence, pattern):
        result = ""
        for i in range(len(sequence)):
            active = list()
            for p in pattern:
                for m in range(0, i+1):
                    active.append(p)
            print(f"PATTERN BUILT")
            iter = 0
            for j in range(len(sequence)):
                # print(f"{sequence[j]}*{active[(j+1)%(4*(i+1))]} + ", end='')
                iter += int(sequence[j])*active[(j+1) % (4*(i+1))]
            result += str(iter)[-1]
            # print(f"FFT RANGE {i} -> {iter}")
        print(f"PHASE: {result}")
        return result

    n = 1
    for i in range(phases):
        # print(f"PHASE {n}, SEQUENCE: {sequence[:100]}...")
        sequence = sequencer(sequence, pattern)
        n += 1

    return sequence


def second():
    pattern = (0, 1, 0, -1)
    print(f"(16.2 test) 98765432109876543210, 7 => {'98765432109876543210'[7:7+8]}")
    sequence = str(DataAnalyzer.load("2019day16.txt")[0])
    offset = int(sequence[:7])
    sequence += 10000 * sequence
    signal = fft(sequence, pattern, 8, 10000)
    print(f"(16.2) {signal[offset:offset+8]}")


def first():
    pattern = (0, 1, 0, -1)
    print(f"(test) {fft('12345678', pattern, 8, 4)}")
    print(f"(test) {fft('80871224585914546619083218645595', pattern, 8, 100)[:8]}")
    print(f"(test) {fft('19617804207202209144916044189917', pattern, 8, 100)[:8]}")

    sequence = str(DataAnalyzer.load("2019day16.txt")[0])
    print(f"(16.1) {fft(sequence, pattern, 8, 100)[:8]}")


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
