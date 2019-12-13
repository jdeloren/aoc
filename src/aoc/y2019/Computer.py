from itertools import repeat

DEFAULT_INCREMENT = 4
INPUT = -1


def amplifier(values, phase, thrusters, signal, amplify):
    global INPUT

    states = {
        # VALUES, INDEX, INPUT, OUTPUT, BASE, COMPLETE
        0: [values.copy(), 0, [phase[0]], 0, 0, False],
        1: [values.copy(), 0, [phase[1]], 0, 0, False],
        2: [values.copy(), 0, [phase[2]], 0, 0, False],
        3: [values.copy(), 0, [phase[3]], 0, 0, False],
        4: [values.copy(), 0, [phase[4]], 0, 0, False]
    }

    active = None
    complete = 1 if amplify else 0

    states[0][2] = [phase[0], signal]

    while complete <= len(thrusters):
        active = 0 if active is None else thrusters[active]
        state = states[active]

        if not state[5]:
            INPUT = state[2]
            output, index, base, done = opcodes(state[0], -1, -1, state[1], amplify)

            state[1] = index
            state[4] = base

            if amplify:
                states[thrusters[active]][2].append(output)
                state[3] = state[3] if done else output

            if done:
                state[3] = state[3] if amplify else output
                state[5] = True
                complete += 1

                if complete <= len(thrusters):
                    states[thrusters[active]][2].append(output)

    # better way to write this?
    return [states[0][3], states[1][3], states[2][3], states[3][3], states[4][3]]


def opcoding(values, identifier, debug=True):
    global INPUT
    INPUT = [identifier]
    output = opcodes(values, -1, -1)
    return output


def opcodes(values, noun, verb, i=0, base=0, feedback=False, debug=False):

    def parameter(n, mode):
        # print(f"MODE: {mode}, INDEX: {index}, REF: {param_index(index, mode)}, BASE: {base}")
        return values[index(n, mode)]

    def index(n, mode):
        return {0: values[n], 1: n, 2: values[n]+base}[mode]

    # EXPERIMENTAL
    if not feedback:
        values.extend(repeat(0, 50000000))

    if noun > 0:
        values[1] = noun
        values[2] = verb

    end = len(values)
    output = 0

    while i < end:
        increment = DEFAULT_INCREMENT
        opcode = values[i]

        mode1 = mode2 = mode3 = 0

        if opcode > 99:
            instructions = str(opcode)
            z = len(instructions)
            opcode = int(instructions[z-2:])
            mode1 = int(instructions[z-3])
            mode2 = int(instructions[z-4]) if z >= 4 else mode2
            mode3 = int(instructions[z-5]) if z >= 5 else mode3

        if opcode == 99:
            print(f"Order 99: {output}")
            break

        op1 = parameter(i+1, mode1)

        if opcode == 1:     # add
            op2 = parameter(i+2, mode2)
            values[index(i+3, mode3)] = op1 + op2
        elif opcode == 2:   # multiply
            op2 = parameter(i+2, mode2)
            values[index(i+3, mode3)] = op1 * op2
        elif opcode == 3:   # store
            global INPUT
            data = int(INPUT.pop(0))
            values[index(i+3, mode3)] = data
            increment = 2
        elif opcode == 4:   # print
            output = op1
            increment = 2
            if feedback:
                return output, i+2, base, False
        elif opcode == 5:   # jump-if-true
            increment = parameter(i+2, mode2) - i if op1 is not 0 else 3
        elif opcode == 6:   # jump-if-false
            increment = parameter(i+2, mode2) - i if op1 is 0 else 3
        elif opcode == 7:   # less-than
            op2 = parameter(i+2, mode2)
            values[index(i+3, mode3)] = 1 if op1 < op2 else 0
        elif opcode == 8:   # equals
            op2 = parameter(i+2, mode2)
            values[index(i+3, mode3)] = 1 if op1 == op2 else 0
        elif opcode == 9:   # relative-base-offset
            base += op1
            increment = 2
        else:
            print("BAD OPCODE: {:d}".format(opcode))
            break

        i = abs(i + increment)

    return output, i, base, True
