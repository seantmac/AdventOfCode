## PART 1

import math
with open('13.TXT') as file:
    earliest = int(file.readline())
    buses = [int(bus) for bus in file.readline().split(',') if bus != 'x']
print("PART ONE " , math.prod(min((bus - earliest % bus, bus) for bus in buses)))


## part 2

with open("13.TXT") as f:
    data = f.readlines()
available = list(map(lambda x: x if x=='x' else int(x), data[1].strip().split(',')))
idmap = {key:val for val, key in filter(lambda x: x[1]!='x', enumerate(available))}
idlist = [id for id in idmap]

step = idlist[0]
start = 0
for id in idlist[1:]:
    delta = idmap[id]
    for i in range(start,step*id,step):
        if not (i+delta)%id:
            step = step*id
            start = i
print("PART TWO " , start)


## AOC 2020 Day 13
## PART ONE  2095
## PART TWO  598411311431841