import numpy as np
from itertools import product


### Functions ###


def decode(mathstring):
    values = []
    levels = []
    level = 0
    for char in mathstring.strip():
        if char == ',':
            continue
        elif char == '[':
            level += 1
        elif char == ']':
            level -= 1
        else:
            values.append(int(char))
            levels.append(level)
    return np.array(values), np.array(levels)


def join(tuple_a, tuple_b):
    a_values, a_levels = tuple_a
    b_values, b_levels = tuple_b
    ab_values = np.append(a_values, b_values)
    ab_levels = np.append(a_levels, b_levels) + 1
    return ab_values, ab_levels


def explode(values, levels):
    check = False
    while np.size(np.where(levels > 4)) > 0:
        check = True
        lpos, rpos, *overflow = np.where(levels > 4)[0]
        if lpos != 0: values[lpos - 1] += values[lpos]
        if rpos != np.size(levels) - 1: values[rpos + 1] += values[rpos]
        values = np.delete(values, (lpos, rpos))
        values = np.insert(values, lpos, 0)
        levels = np.delete(levels, (lpos, rpos))
        levels = np.insert(levels, lpos, 4)
    return values, levels, check


def split(values, levels):
    check = False
    if np.size(np.where(values > 9)) > 0:
        check = True
        pos, *overflow = np.where(values > 9)[0]
        lval, rval = np.floor(values[pos] / 2), np.ceil(values[pos] / 2)
        level = levels[pos] + 1
        values = np.delete(values, pos)
        values = np.insert(values, pos, (lval, rval))
        levels = np.delete(levels, pos)
        levels = np.insert(levels, pos, (level, level))
    return values, levels, check


def magnitude(values, levels):
    if np.size(values) > 1:
        lpos, rpos, *overflow = np.where(levels == levels.max())[0]
        val = values[lpos] * 3 + values[rpos] * 2
        level = levels[lpos] - 1
        values = np.delete(values, (lpos, rpos))
        values = np.insert(values, lpos, val)
        levels = np.delete(levels, (lpos, rpos))
        levels = np.insert(levels, lpos, level)
        values, levels = magnitude(values, levels)
    return values, levels


### Part 1 ###


with open('18.TXT', 'r') as file:
    data = file.read().split('\n')

values, levels = decode(data[0])

for mathstring in data[1:]:
    values, levels = join((values, levels), decode(mathstring))
    check_explode = True
    check_split = True
    while check_explode or check_split:
        values, levels, check_explode = explode(values, levels)
        values, levels, check_split = split(values, levels)

print(magnitude(values, levels)[0][0])

### Part 2 ###


magnitude_list = []

for i, j in product(range(len(data)), range(len(data))):
    if i == j: continue

    values, levels = join(decode(data[i]), decode(data[j]))
    check_explode = True
    check_split = True
    while check_explode or check_split:
        values, levels, check_explode = explode(values, levels)
        values, levels, check_split = split(values, levels)
    magnitude_list.append(magnitude(values, levels)[0][0])

    values, levels = join(decode(data[j]), decode(data[i]))
    check_explode = True
    check_split = True
    while check_explode or check_split:
        values, levels, check_explode = explode(values, levels)
        values, levels, check_split = split(values, levels)
    magnitude_list.append(magnitude(values, levels)[0][0])

print(max(magnitude_list))


#3305
#4563