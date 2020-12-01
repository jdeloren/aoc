#!/usr/bin/python
from src.aoc.common import DataAnalyzer
import sys


def cut(deck: list, point: int):
    print(f"CUT {point}")
    return deck[point:] + deck[:point]


def deal(deck: list, inc: int):
    print(f"DEAL {inc}")
    table = [None] * len(deck)
    i, j = 0, 0
    while None in table:
        # print(f"DEAL INTO {i} {len(table)} {j} {len(deck)}")
        if table[i] is not None:
            print(f"TABLE SPOT TAKEN?? {j} of {len(deck)}")
            exit(1)
        table[i] = deck[j]
        i = (i + inc) % len(table)
        j += 1
    return table


def stack(deck: list):
    print(f"STACK")
    return list(reversed(deck))


def run_instructions(values: list, deck: list):
    print("INSTRUCTION SET")
    for value in values:
        if value.endswith('stack'):
            deck = stack(deck)
        elif value.startswith('deal'):
            deck = deal(deck, int(value.split(' ')[-1]))
        elif value.startswith('cut'):
            deck = cut(deck, int(value.split(' ')[-1]))

    return deck


def repeat_instructions(values: list, count: int = 101741582076661):
    # deck = [x for x in range(119315717514047 // 1000000003)]
    shoe = list()

    deck = [x for x in range(119315)]
    positions = []

    print("STARTING LOOP")
    for i in range(count):
        out = run_instructions(values, deck)
        if out in positions:
            print(f"REPEATED ORDER AT: {len(positions)}")
        if len(positions) % 10 == 0:
            print(f"SETS DONE: {len(positions)}")

        positions.append(out.copy())
        deck = out

    return deck


def second():
    values = [i.strip() for i in DataAnalyzer.load("2019day22.txt")]
    deck = repeat_instructions(values)
    print(f"(22.1) Position of cards 2019 is {deck.index(2020)}")


def first():
    values = [i.strip() for i in DataAnalyzer.load("2019day22.txt")]
    deck = run_instructions(values, [x for x in range(10007)])
    print(f"(22.1) Position of cards 2019 is {deck.index(2019)}")


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
