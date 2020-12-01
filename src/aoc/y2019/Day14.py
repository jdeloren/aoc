#!/usr/bin/python
from src.aoc.common import DataAnalyzer
import math
import sys


def calculate(values, source, target):
    formulae = formulas(values)
    stack = [x for x in formulae['FUEL'][1:]]
    print(f"INIT STACK: {stack}")
    stockpile = (stacker(dict(), dict(), stack, formulae, 'ORE', 'FUEL'))
    print(f"STOCKPILE: {stockpile[0]}, UNUSED: {stockpile[1]}")

    total = 0
    # relies on everything in stockpile being a base target component (e.g. 'ORE')
    for key, value in stockpile[0].items():
        item = formulae[key]
        total += math.ceil(value / item[0]) * item[1]

    print(f"1 {target} requires {total} {source}")


def stacker(stockpile, unused, stack, formulae, source, target):
    def push(mult, formula):
        for f in range(1, len(formula), 2):
            if formula[f+1] in stack:
                stack[stack.index(formula[f+1])-1] += (formula[f] * mult)
            else:
                stack.insert(0, formula[f+1])
                stack.insert(0, formula[f] * mult)

    while len(stack) > 0:
        item = stack[:2]
        del stack[:2]
        material = formulae[item[1]]

        if item[1] in unused:
            if unused[item[1]] > item[0]:
                unused[item[1]] -= item[0]
            else:
                item[0] -= unused[item[1]]
                del unused[item[1]]

        if item[0] > 0:
            if material[2] == source:
                stockpile[item[1]] = stockpile.get(item[1], 0) + int(item[0])
            else:
                if item[0] < material[0]:
                    div = 1
                    extra = material[0] - item[0]
                else:
                    div = math.ceil(item[0] / material[0])
                    extra = material[0] * div - item[0]

                push(div, formulae[item[1]])
                unused[item[1]] = unused.get(item[1], 0) + extra

        # print(f"stacking with {stack}, stockpile: {stockpile}")
        return stacker(stockpile, unused, stack, formulae, source, target)

    return stockpile, unused, stack


def formulas(equations):
    # key will be element name at end of formula to ease lookups, 1st element in value is generated amount
    formulae = dict()

    for equation in equations:
        values = list()
        components = equation.replace(',', '').split(' ')

        for i in range(0, len(components), 2):
            values.extend([int(components[i]), components[i+1]])
            if components[i+2] == '=>':  # pull key, then update list
                values.insert(0, int(components[i+3]))
                formulae[components[i+4]] = values.copy()
                break

    return formulae


def second():
    values = DataAnalyzer.load("2019day14.txt")


def first():
    # values = [
    #     "9 ORE => 2 A",
    #     "8 ORE => 3 B",
    #     "7 ORE => 5 C",
    #     "3 A, 4 B => 1 AB",
    #     "5 B, 7 C => 1 BC",
    #     "4 C, 1 A => 1 CA",
    #     "2 AB, 3 BC, 4 CA => 1 FUEL"
    # ]
    # calculate(values, 'ORE', 'FUEL')

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
    # calculate(values, 'ORE', 'FUEL')
    #
    # values = [
    #     "2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG",
    #     "17 NVRVD, 3 JNWZP => 8 VPVL",
    #     "53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL",
    #     "22 VJHF, 37 MNCFX => 5 FWMGM",
    #     "139 ORE => 4 NVRVD",
    #     "144 ORE => 7 JNWZP",
    #     "5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC",
    #     "5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV",
    #     "145 ORE => 6 MNCFX",
    #     "1 NVRVD => 8 CXFTF",
    #     "1 VJHF, 6 MNCFX => 4 RFSQX",
    #     "176 ORE => 6 VJHF"
    # ]
    # calculate(values, 'ORE', 'FUEL')
    # #
    values = [
        "171 ORE => 8 CNZTR",
        "7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL",
        "114 ORE => 4 BHXH",
        "14 VRPVC => 6 BMBT",
        "6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL",
        "6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT",
        "15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW",
        "13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW",
        "5 BMBT => 4 WPTQ",
        "189 ORE => 9 KTJDG",
        "1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP",
        "12 VRPVC, 27 CNZTR => 2 XDBXC",
        '15 KTJDG, 12 BHXH => 5 XCVML',
        "3 BHXH, 2 VRPVC => 7 MZWV",
        "121 ORE => 7 VRPVC",
        "7 XCVML => 6 RJRHP",
        "5 BHXH, 4 VRPVC => 5 LTCX"
    ]
    calculate(values, 'ORE', 'FUEL')

    # values = DataAnalyzer.load("2019day14.txt")
    # values = [x.strip() for x in values]
    # print(values)
    # calculate(values, 'ORE', 'FUEL')


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    solve(sys.argv[1])
