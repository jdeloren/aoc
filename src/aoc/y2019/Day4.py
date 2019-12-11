def passcode(digits, limiter=False):
    data = str(digits)

    repeats = 0
    repeat = False
    increase = True

    last = data[0]
    for i in range(1, len(data)):
        if data[i] == last:
            repeat = True if not limiter else repeat
            repeats += 1
        else:
            repeat = True if (repeats == 1) else repeat
            repeats = 0

        if i == len(data)-1 and repeats == 1:
            repeat = True
            break

        if data[i] < last:
            increase = False
            break

        last = data[i]

    return repeat and increase


def second():
    inputs = "183564-657474"
    data = inputs.split("-")

    valid = 0
    for i in range(int(data[0]), int(data[1])+1):
        valid += 1 if passcode(i, True) else 0

    print("(4.2) Valid phrases: {:d}".format(valid))


def first():
    inputs = "183564-657474"
    data = inputs.split("-")

    valid = 0
    for i in range(int(data[0]), int(data[1])+1):
        valid += 1 if passcode(i) else 0

    print("(4.1) Valid phrases: {:d}".format(valid))


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
