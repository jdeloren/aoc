DEFAULT_INCREMENT = 4
INPUT = -1


def amplifier(values, phase, thrusters, signal, amplify):
    global INPUT

    states = {
        # VALUES, INDEX, INPUT, FINAL OUTPUT
        0: [values.copy(), 0, [phase[0]], None],
        1: [values.copy(), 0, [phase[1]], None],
        2: [values.copy(), 0, [phase[2]], None],
        3: [values.copy(), 0, [phase[3]], None],
        4: [values.copy(), 0, [phase[4]], None]
    }

    # WORKING!
    # thruster = list()
    # output = None
    # for num in phase:
    #     SHADE = [num, output[0] if output is not None else signal]
    #     PHASE = num
    #     output = opcodes(values.copy(), -1, -1)
    #
    #     if output[0] != OUTPUT:
    #         print("OUTPUT diff: {:d} vs {:d}".format(output[0], OUTPUT))
    #
    #     thruster.append(output[0])
    #
    # return thruster

    active = None
    complete = 1 if amplify else 0

    # only for part1??
    states[0][2] = [phase[0], signal]

    while complete <= len(thrusters):
        active = 0 if active is None else thrusters[active]
        state = states[active]

        if state[3] is None:
            INPUT = state[2]
            print("Thruster: {:d}, input: ({:s}), index: {:d}".format(active, ' '.join(map(str, INPUT)), state[1]))
            output, index, done = opcodes(state[0], -1, -1, state[1], amplify)

            state[1] = index

            if amplify:
                states[thrusters[active]][2].append(output)

            if done:
                state[3] = output
                complete += 1

                if complete <= len(thrusters):
                    states[thrusters[active]][2].append(output)

    # better way to write this?
    print("{:d} {:d} {:d} {:d} {:d}".format(states[0][3], states[1][3], states[2][3], states[3][3], states[4][3]))
    return [states[0][3], states[1][3], states[2][3], states[3][3], states[4][3]]


def opcoding(values, identifier, debug=True):
    global INPUT
    INPUT = [identifier]
    output = opcodes(values, -1, -1)

    if debug:
        print(output[0])

    return output


def parameter(values, index, mode):
    value = values[index]
    return values[value] if mode == 0 else value


def opcodes(values, noun, verb, i=0, feedback=False):
    if noun > 0:
        values[1] = noun
        values[2] = verb

    end = len(values)
    output = 0

    while i < end:
        increment = DEFAULT_INCREMENT
        opcode = values[i]

        mode1 = 0
        mode2 = 0

        if opcode > 99:
            instructions = str(opcode)
            length = len(instructions)
            opcode = int(instructions[length-2:])
            mode1 = int(instructions[length-3])
            mode2 = int(instructions[length-4]) if length == 4 else mode2

        if opcode == 99:
            break

        op1 = parameter(values, i+1, mode1)

        if opcode == 1:     # add
            op2 = parameter(values, i+2, mode2)
            values[values[i+3]] = op1 + op2
        elif opcode == 2:   # multiply
            op2 = parameter(values, i+2, mode2)
            values[values[i+3]] = op1 * op2
        elif opcode == 3:   # store
            global INPUT
            data = int(INPUT.pop(0))
            values[values[i+1]] = data
            print("Using input: {:d}".format(data))
            increment = 2
        elif opcode == 4:   # print
            output = op1
            increment = 2
            if feedback:
                # print("Simulated pause on print: {:d}".format(output))
                return output, i+2, False
        elif opcode == 5:   # jump-if-true
            increment = parameter(values, i+2, mode2) - i if op1 is not 0 else 3
        elif opcode == 6:   # jump-if-false
            increment = parameter(values, i+2, mode2) - i if op1 is 0 else 3
        elif opcode == 7:   # less-than
            op2 = parameter(values, i+2, mode2)
            values[values[i+3]] = 1 if op1 < op2 else 0
        elif opcode == 8:   # equals
            op2 = parameter(values, i+2, mode2)
            values[values[i+3]] = 1 if op1 == op2 else 0
        else:
            print("BAD OPCODE: {:d}".format(opcode))
            break

        i = abs(i + increment)

    # if feedback:
    #     print("Final output: {:d}".format(output))

    return output, i, True
