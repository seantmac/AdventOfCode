class Intcomp():
    def __init__(self, code: list, mode='default'):
        self.code = None
        self.orig_code = None
        self.load(code)
        self.ip = 0
        self.rel_base = 0
        self.num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
        self.out = []
        self.mode = mode
        self.halt = False

    def load(self, code: list):
        self.orig_code = code
        self.code = defaultdict(int, enumerate(code))

    def set(self, code: list = None, pointer: int = None, base: int = None):
        if code is not None:
            self.load(code)
        self.ip = pointer if pointer is not None else self.ip
        self.rel_base = base if base is not None else self.rel_base

    def reset(self):
        self.set(code=self.orig_code, pointer=0, base=0)
        self.out = []

    def clear_output(self):
        self.out = []

    def run(self, inp: int = 0):
        self.halt = False
        while self.code[self.ip] != 99 and not self.halt:
            modes = [int(x) for x in f"{self.code[self.ip]:0>5}"[:3]][::-1]
            instruction = int(f"{self.code[self.ip]:0>5}"[3:])
            operands = [0 for _ in range(self.num_of_operands[instruction])]
            adjust = [0 for _ in range(self.num_of_operands[instruction])]
            for m in range(self.num_of_operands[instruction]):
                if modes[m] == 0:
                    operands[m] = self.code[self.code[self.ip + m + 1]]
                elif modes[m] == 1:
                    operands[m] = self.code[self.ip + m + 1]
                elif modes[m] == 2:
                    adjust[m] = self.rel_base
                    operands[m] = self.code[self.rel_base + self.code[self.ip + m + 1]]

            if instruction == 1:  # ADD
                self.code[adjust[2] + self.code[self.ip + 3]] = operands[0] + operands[1]
            elif instruction == 2:  # MULTIPLY
                self.code[adjust[2] + self.code[self.ip + 3]] = operands[0] * operands[1]
            elif instruction == 3:  # INPUT
                self.code[adjust[0] + self.code[self.ip + 1]] = inp
            elif instruction == 4:  # OUTPUT
                self.out.append(operands[0])
                if self.mode == 'paint' and len(self.out) == 2:
                    self.halt = True
            elif instruction == 5:  # JUMP IF TRUE
                self.ip = (operands[1] - 3) if operands[0] != 0 else self.ip
            elif instruction == 6:  # JUMP IF FALSE
                self.ip = (operands[1] - 3) if operands[0] == 0 else self.ip
            elif instruction == 7:  # TRUE IS LESS THAN
                self.code[adjust[2] + self.code[self.ip + 3]] = int(operands[0] < operands[1])
            elif instruction == 8:  # TRUE IF EQUAL
                self.code[adjust[2] + self.code[self.ip + 3]] = int(operands[0] == operands[1])
            elif instruction == 9: # INCREASE RELATIVE BASE
                self.rel_base += operands[0]
            self.ip += self.num_of_operands[instruction] + 1
        return self.out