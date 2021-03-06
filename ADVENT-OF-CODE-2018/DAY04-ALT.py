# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:44:22 2018

@author: SMACDER
"""

from collections import Counter, defaultdict
from datetime import datetime

s= open("4.TXT").read().split("\n")

guards = defaultdict(Counter)
for t, m in [l.split('] ') for l in sorted(s) if l]:
    t = datetime.strptime(t, '[%Y-%m-%d %H:%M')
    if '#' in m:     g = int(m.split('#')[1].split()[0])
    if 'falls' in m: start = t
    if 'wakes' in m:
        minutes = int((t - start).total_seconds() // 60)
        guards[g].update(Counter((start.minute+i)%60 for i in range(minutes)))

_, id = max((sum(c.values()), id) for id, c in guards.items())
part1 = id * guards[id].most_common()[0][0]

(_, minute), id = max((c.most_common()[0][::-1], id) for id, c in guards.items())
part2 = id * minute

print("Part1:  " + str(part1))
print("Part2:  " + str(part2))

#CORRECT
#Part1:  65489
#Part2:  3852