#!/usr/bin/env python

from collections import defaultdict
import itertools

def get_happy(graph):
    totals = defaultdict(int)
    for perm in itertools.permutations(graph.keys()):
        for i, _ in enumerate(perm):
            n1 = perm[i]
            n2 = perm[(i+1) % len(perm)]
            totals[perm] += graph[n1][n2]
            totals[perm] += graph[n2][n1]

    mp = max(totals, key=totals.get)
    return mp, totals[mp]

with open('13.TXT') as fd:
    lines = [line.strip() for line in fd]

graph = defaultdict(dict)
for line in lines:
    # format: "Bob would lose 14 happiness units by sitting next to Alice."
    name1, _, sign, amount, _, _, _, _, _, _, name2 = line.split()
    name2 = name2.split('.')[0]
    amount = int(amount) if sign == 'gain' else -int(amount)
    graph[name1][name2] = amount

p, total = get_happy(graph)
print('part one: {} -> {}'.format(p, total))

# add myself
for k in graph.keys():
    graph['me'][k] = 0
    graph[k]['me'] = 0

p, total = get_happy(graph)
print('part two: {} -> {}'.format(p, total))