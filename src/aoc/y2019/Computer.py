from itertools import repeat
import sys


class IntCode:
    def __init__(self, values, input_list=None, input_func=None, extend=False, interrupt=False, auto=False, x=5000000):
        if input_list is None:
            input_list = []

        self.codes = values.copy()
        self.interrupt = interrupt
        self.address = 0
        self.done = False
        self._extension = x
        self._debug = False
        self._debug_out = sys.stdout
        self._init(input_list, input_func)

        if extend:
            self.codes.extend(repeat(0, self._extension))

        self.backup = self.codes.copy()

        if auto:
            self.start()

    def debug(self, debug, file=None):
        self._debug = debug
        self._debug_out = self._debug_out if file is None else file

    def _print(self, string):
        if self._debug:
            print(string, file=self._debug_out)

    def inputs(self, data):
        self._inputs.append(data)

    def output(self, size=0):
        if size == 0:
            size = len(self._output)

        requested = self._output[:size]
        del self._output[:size]
        return requested

    def _init(self, input_list=None, input_func=None):
        self.base = 0
        self.address = 0
        self._inputs = list() if input_list is None else input_list
        self._inputter = input_func
        self._output = []
        self.done = False

    def reset(self, input_list=None, input_func=None):
        self.codes = self.backup
        self._init(input_list, input_func)

    def start(self):
        def _parameter(n, mode):
            # print(f"MODE: {mode}, INDEX: {index}, REF: {param_index(index, mode)}, BASE: {base}")
            return self.codes[_index(n, mode)]

        def _index(n, mode):
            return {0: self.codes[n], 1: n, 2: self.codes[n] + self.base}[mode]

        end = len(self.codes)

        while self.address < end:
            increment = 4
            opcode = self.codes[self.address]

            mode1 = mode2 = mode3 = 0

            if opcode > 99:
                # todo - bake this into parameter function
                instructions = str(opcode).zfill(5)
                opcode = int(instructions[3:])
                mode1 = int(instructions[2])
                mode2 = int(instructions[1])
                mode3 = int(instructions[0])

            if opcode == 99:
                self.done = True
                self._print(f"Order 99: {self._output}")
                break

            op1 = _parameter(self.address + 1, mode1)

            if opcode == 1:  # add
                op2 = _parameter(self.address + 2, mode2)
                self.codes[_index(self.address + 3, mode3)] = op1 + op2
                self._print(f"OPCODE 1: {op1} {op2} @ {_index(self.address + 3, mode3)}")
            elif opcode == 2:  # multiply
                op2 = _parameter(self.address + 2, mode2)
                self.codes[_index(self.address + 3, mode3)] = op1 * op2
                self._print(f"OPCODE 2: {op1} {op2} @ {_index(self.address + 3, mode3)}")
            elif opcode == 3:  # store
                data = self._inputter() if self._inputter else int(self._inputs.pop(0))
                self._print(f"OPCODE 3: {data} -> {_index(self.address + 1, mode1)}")
                self.codes[_index(self.address + 1, mode1)] = data
                increment = 2
            elif opcode == 4:  # print
                self._output.append(op1)
                self._print(f"OPCODE 4: {op1}")
                increment = 2
                if self.interrupt:
                    self.address += increment
                    return self._output

            elif opcode == 5:  # jump-if-true
                increment = _parameter(self.address + 2, mode2) - self.address if op1 is not 0 else 3
                self._print(f"OPCODE 5: {increment+self.address}")
            elif opcode == 6:  # jump-if-false
                increment = _parameter(self.address + 2, mode2) - self.address if op1 is 0 else 3
                self._print(f"OPCODE 6: {increment+self.address}")
            elif opcode == 7:  # less-than
                op2 = _parameter(self.address + 2, mode2)
                self.codes[_index(self.address + 3, mode3)] = 1 if op1 < op2 else 0
                self._print(f"OPCODE 7: {op1} {op2} @ {_index(self.address + 3, mode3)}")
            elif opcode == 8:  # equals
                op2 = _parameter(self.address + 2, mode2)
                self.codes[_index(self.address + 3, mode3)] = 1 if op1 == op2 else 0
                self._print(f"OPCODE 8: {op1} {op2} @ {_index(self.address + 3, mode3)}")
            elif opcode == 9:  # relative-base-offset
                self.base += op1
                increment = 2
                self._print(f"OPCODE 9: {op1} -> {self.base}")
            else:
                print("BAD OPCODE: {:d}".format(opcode))
                break

            self.address = abs(self.address + increment)

        return self._output
