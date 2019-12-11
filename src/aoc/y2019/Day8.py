from aoc import DataAnalyzer


def printer(encoded):
    for char in encoded:
        if char == 0:
            return ' '
        elif char == 1:
            return '*'

    return ' '


def decode(layers, width, height):
    for n in range(height):
        for m in range(width):
            stack = [int(i[n*width+m]) for i in layers]
            print(printer(stack), end='')
        print("")
    print("")


def imaging(values, width=25, height=6):
    size = height * width
    layers = list()

    for i in range(len(values) // size):
        index_a = i * size
        index_b = (i * size) + size
        layers.append(values[index_a:index_b])

    return layers


def layer_with_fewest(values, target='0'):
    fewest = len(values[0])
    entry = None

    for i in values:
        result = str(i).count(target)
        if result < fewest:
            entry = i
            fewest = result

    return entry, fewest


def second():
    values = '0222112222120000'
    layers = imaging(values, 2, 2)
    decode(layers, 2, 2)

    values = DataAnalyzer.load("2019day8.txt")
    layers = imaging(values[0][:-1])
    decode(layers, 25, 6)


def first():
    values = DataAnalyzer.load("2019day8.txt")
    layers = imaging(values[0][:-1])
    image, count = layer_with_fewest(layers, '0')
    print("At fewest 0's of {:d}, 1's * 2's is {:d}".format(count, (image.count('1') * image.count('2'))))


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
