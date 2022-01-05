#And now for Part 2. I did a lot of little tests when I started writing out the classes
# because I forgot how they worked. Then when I figured out how to make the class right,
# I wrote all the functions in one go without testing anything. Then spent like 2 hours
# debugging. Whee!

#Luckily for me though, the first time the program went through without
# raising an unhandled exception it gave me the right answer. Phew.

###   ALL THANKS TO https://www.reddit.com/user/hugseverycat   ###

#Part 2:

registers = {}
instructions = []


class Program:
    def __init__(self, p_id):
        self.id = p_id
        self.instruction = 0
        self.register = {}
        self.queue = []
        self.paused = False
        self.send_count = 0

    def receive_register(self, reg):
        try:
            self.register[reg] = self.queue.pop(0)
            self.paused = False
            self.instruction += 1
        except IndexError:
            self.paused = True

    def send_register(self, reg):
        if self.id == 1:
            destination_program = program_list[0]
        else:
            destination_program = program_list[1]
        destination_program.queue.append(self.register[reg])
        self.instruction += 1
        self.send_count += 1

    def set_register(self, reg, value):
        # value might be an integer or a register
        try:
            self.register[reg] = self.register[value]
        except KeyError:
            self.register[reg] = value
        self.instruction += 1

    def add_register(self, reg, value):
        # value might be an integer or a register
        try:
            self.register[reg] += self.register[value]
        except KeyError:
            self.register[reg] += value
        self.instruction += 1

    def mult_register(self, reg, value):
        # value might be an integer or a register
        try:
            self.register[reg] *= self.register[value]
        except KeyError:
            self.register[reg] *= value
        self.instruction += 1

    def mod_register(self, reg, value):
        # value might be an integer or a register
        try:
            self.register[reg] %= self.register[value]
        except KeyError:
            self.register[reg] %= value
        self.instruction += 1

    def jump_register(self, reg, value):
        # value might be an integer or a register
        try:
            if self.register[reg] > 0:
                try:
                    self.instruction += value
                except TypeError:
                    self.instruction += self.register[value]
            else:
                self.instruction += 1
        except KeyError:  # reg might be an integer or a register too :(
            if reg > 0:
                try:
                    self.instruction += value
                except TypeError:
                    self.instruction += self.register[value]
            else:
                self.instruction += 1

    def do_next_instruction(self):
        this_instruction = instructions[self.instruction]
        i_reg = this_instruction[1]
        try:
            i_value = this_instruction[2]
        except IndexError:
            i_value = None
        if not self.paused:
            if this_instruction[0] == "snd":
                self.send_register(i_reg)
            elif this_instruction[0] == "set":
                self.set_register(i_reg, i_value)
            elif this_instruction[0] == "add":
                self.add_register(i_reg, i_value)
            elif this_instruction[0] == "mul":
                self.mult_register(i_reg, i_value)
            elif this_instruction[0] == "mod":
                self.mod_register(i_reg, i_value)
            elif this_instruction[0] == "rcv":
                self.receive_register(i_reg)
            if this_instruction[0] == "jgz":
                self.jump_register(i_reg, i_value)
        else:
            if this_instruction[0] == "rcv":
                self.receive_register(i_reg)


program_list = [Program(i) for i in range(0, 2)]


with open("18.TXT") as f:
    for line in f:
        this_line = line.strip().split(' ')

        for i in range(0, len(this_line)):
            try:
                this_line[i] = int(this_line[i])
            except ValueError:
                if i == 1:
                    program_list[0].register[this_line[i]] = 0
                    program_list[1].register[this_line[i]] = 0
        instructions.append(this_line)
    program_list[0].register['p'] = 0
    program_list[1].register['p'] = 1

while not (program_list[0].paused and program_list[1].paused):
    program_list[0].do_next_instruction()
    program_list[1].do_next_instruction()


print("Part 2: " + str(program_list[1].send_count))
