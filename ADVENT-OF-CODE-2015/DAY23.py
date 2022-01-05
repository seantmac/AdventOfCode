program = [i.strip().split(' ', 1) for i in open('23.TXT').readlines()]

registers = {'a': 0, 'b': 0, 'pc': 0}


def hlf(args):
    registers[args] >>= 1
    registers['pc'] += 1


def tpl(args):
    registers[args] *= 3
    registers['pc'] += 1


def inc(args):
    registers[args] += 1
    registers['pc'] += 1


def jmp(args):
    registers['pc'] += int(args)


def jie(args):
    r, o = args.split(', ')
    if registers[r] % 2 == 0:
        registers['pc'] += int(o)
    else:
        registers['pc'] += 1


def jio(args):
    r, o = args.split(', ')
    if registers[r] == 1:
        registers['pc'] += int(o)
    else:
        registers['pc'] += 1


instructions = {'hlf': hlf, 'tpl': tpl, 'inc': inc, 'jmp': jmp, 'jie': jie, 'jio': jio}

# Part 1
registers = {'a': 0, 'b': 0, 'pc': 0}

while registers['pc'] < len(program):
    instructions[program[registers['pc']][0]](program[registers['pc']][1])
registers
print('1 ', registers)

# Part 2
registers = {'a': 1, 'b': 0, 'pc': 0}

while registers['pc'] < len(program):
    instructions[program[registers['pc']][0]](program[registers['pc']][1])
registers
print('2 ', registers)

#1:  307
#2:  160
#1  {'a': 1, 'b': 307, 'pc': 47}
#2  {'a': 1, 'b': 160, 'pc': 47}