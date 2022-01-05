#Hooray! After a frustrating weekend I have a puzzle I solved without looking at reddit.

#Used different code for parts 1 and 2, so they will be in two bits. Part 2 creates two Program objects and runs
# them simultaneously. They keep track of whether they are paused or not, and when both programs are paused, it ends.

###   ALL THANKS TO https://www.reddit.com/user/hugseverycat   ###

#Part 1:

registers = {}
instructions = []
last_sound = None
recover = False
instruction_counter = 0

with open("18.TXT") as f:
    for line in f:
        this_line = line.strip().split(' ')

        for i in range(0, len(this_line)):
            try:
                this_line[i] = int(this_line[i])
            except ValueError:
                if i == 1:
                    registers[this_line[i]] = 0
        instructions.append(this_line)


def play_sound(register):
    return registers[register]


def set_register(register, value):
    try:
        registers[register] = registers[value]
    except KeyError:
        registers[register] = value


def add_register(register, value):
    try:
        registers[register] += registers[value]
    except KeyError:
        registers[register] += value


def mult_register(register, value):
    try:
        registers[register] *= registers[value]
    except KeyError:
        registers[register] *= value


def mod_register(register, value):
    try:
        registers[register] %= registers[value]
    except KeyError:
        registers[register] %= value


def jump_register(register, value):
    if registers[register] > 0:
        return value
    else:
        return 1


while not recover:
    this_instruction = instructions[instruction_counter]

    if this_instruction[0] == "snd":
        last_sound = play_sound(this_instruction[1])
    elif this_instruction[0] == "set":
        set_register(this_instruction[1], this_instruction[2])
    elif this_instruction[0] == "add":
        add_register(this_instruction[1], this_instruction[2])
    elif this_instruction[0] == "mul":
        mult_register(this_instruction[1], this_instruction[2])
    elif this_instruction[0] == "mod":
        mod_register(this_instruction[1], this_instruction[2])
    elif this_instruction[0] == "rcv":
        if registers[this_instruction[1]] != 0:
            recover = True

    if this_instruction[0] == "jgz":
        instruction_counter += jump_register(this_instruction[1], this_instruction[2])
    else:
        instruction_counter += 1

print("Part 1: " + str(last_sound))
