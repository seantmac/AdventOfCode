#!/usr/bin/env python3

STRING = open('10.TXT').read()
if STRING[-1] == '\n':
    STRING = STRING[:-1]

answer1 = STRING

for i in range(40):
    new = ''
    s = 0
    while s < len(answer1):
        c = answer1[s]
        n = 1
        s += 1
        while s < len(answer1) and answer1[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    answer1 = new

print(len(answer1))

answer2 = answer1

for i in range(10):
    new = ''
    s = 0
    while s < len(answer2):
        c = answer2[s]
        n = 1
        s += 1
        while s < len(answer2) and answer2[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    answer2 = new

print(len(answer2))


#360154
#5103798