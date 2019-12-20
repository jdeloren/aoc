#!/usr/bin/python
from src.aoc.common import DataAnalyzer
import math
import sys


def calculate(formulae, stockpile, source, target):
    total = 0
    # relies on everything in stockpile being a base target component (e.g. 'ORE')
    for key, value in stockpile.items():
        item = formulae[key]
        total += math.ceil(value / int(item[0])) * int(item[1][0])

    print(f"1 {target} requires {total} {source}")


def stacker(used, unused, stack, formulae, source, target):
    def counter(component, required, produced):
        # return 1 if required < produced else required // produced
        if required < produced:
            unused[component] = unused.get(component, 0) + produced - required
            # print(f"{component} has {produced} - {required} left over, now {unused[component]}")
            print(unused)
            return 1

        return required // produced

    while len(stack) > 0:
        item = stack.pop(0)
        material = formulae[item[1]]
        # print(f"I need: {item[0]} {item[1]}, formula: {material}, unused: {unused}")

        # if unused.get(material[1][1], 0):
        #     print(f"SURPLUS {item[1]}: {unused.get(item[1], 0)}")

        if material[1][1] == source:
            total = int(item[0]) * int(material[1][0])
            used[material[1][1]] = used.get(material[1][1], 0) + math.ceil(total / int(material[0]))
            unused[material[1][1]] = unused.get(material[1][1], 0) + total % int(material[0])
            # print(f"{item[1]} takes {material[1][0]} {material[1][1]}.  Using {total} {material[1][1]}, {total % int(material[0])} remaining")
            print(f"TOTAL: {total}, MATERIAL: {material[1]}, PRODUCED: {math.ceil(total / int(material[0]))}, LEFTOVER: {total % int(material[0])}")
            print(f"USED: {used}, UNUSED: {unused}")
        else:
            div = counter(item[1], int(item[0]), int(material[0]))
            stack = [(div * int(x[0]), x[1]) for x in formulae[item[1]][1:]] + stack

        print(f"stacking with {stack}")
        return stacker(used, unused, stack, formulae, source, target)

    return used, unused, stack


def generator(formulae, stockpile, source, target, base):
    # print(f"GENERATOR: {stockpile} {source} {target}")
    if target != source:
        components = formulae[target].copy()
        amount = int(components.pop(0))    # elements list is now only required pairs in formula

        for component in components:
            if component[1] == source:
                return amount
            else:
                generated = generator(formulae, stockpile, source, component[1], int(component[0]))

                if isinstance(generated, int):
                    # print(f"Adding {base} * {component[0]} of {component[1]}")
                    # print(f"base {base}, {generated} * {int(component[0])} => {base * int(component[0])} {component[1]}")
                    stockpile[component[1]] = stockpile.get(component[1], 0) + base * int(component[0])

    return stockpile


def formulas(equations):
    # key will be element name at end of formula to ease lookups, 1st element in value is generated amount
    formulae = dict()

    for equation in equations:
        values = list()
        components = equation.replace(',', '').split(' ')

        for i in range(0, len(components), 2):
            values.append((components[i], components[i+1]))
            if components[i+2] == '=>':  # pull key, then update list
                values.insert(0, components[i+3])
                formulae[components[i+4]] = values.copy()
                break

    print(formulae)
    return formulae


def second():
    values = DataAnalyzer.load("2019day14.txt")


def first():
    values = [
        "9 ORE => 2 A",
        "8 ORE => 3 B",
        "7 ORE => 5 C",
        "3 A, 4 B => 1 AB",
        "5 B, 7 C => 1 BC",
        "4 C, 1 A => 1 CA",
        "2 AB, 3 BC, 4 CA => 1 FUEL"
    ]

    formulae = formulas(values)
    # print("GENERATOR func:")
    # stockpile = generator(formulae, dict(), 'ORE', 'FUEL', 1)
    # print(stockpile)
    # calculate(formulae, stockpile, 'ORE', 'FUEL')
    print("STACKER func:")
    stack = [x for x in formulae['FUEL'][1:]]
    print(stack)
    used, unused, stack = (stacker(dict(), dict(), stack, formulae, 'ORE', 'FUEL'))
    print(f"1 FUEL requires {int(used['ORE']) + int(unused['ORE'])} ORE")


    # values = [
    #     "157 ORE => 5 NZVS",
    #     "165 ORE => 6 DCFZ",
    #     "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
    #     "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ",
    #     "179 ORE => 7 PSHF",
    #     "177 ORE => 5 HKGWZ",
    #     "7 DCFZ, 7 PSHF => 2 XJWVT",
    #     "165 ORE => 2 GPVTF",
    #     "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"
    # ]
    # formulae = formulas(values)
    # print("STACKER func:")
    # stack = [x for x in formulae['FUEL'][1:]]
    # print(stack)
    # used, unused, stack = (stacker(dict(), dict(), stack, formulae, 'ORE', 'FUEL'))
    # print(f"1 FUEL requires {int(used['ORE']) + int(unused['ORE'])} ORE")

    # print(f"Formula count: {len(formulae)}")
    # stockpile = generator(formulae, dict(), 'ORE', 'FUEL', 1)
    # print(stockpile)
    # calculate(formulae, stockpile, 'ORE', 'FUEL')

    # values = DataAnalyzer.load("2019day14.txt")


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
