from itertools import combinations
from math import prod

with open('1.TXT', 'r') as f:
    entries = [int(i) for i in f.read().strip().splitlines()]

solution = lambda k: next( prod(comb) for comb in combinations(entries, k) if sum(comb) == 2020 )
print (solution(2), solution(3))

#1005459 92643264