#!/usr/bin/env python3

from itertools import combinations
from functools import reduce

quantumentanglement = lambda g: reduce(int.__mul__, g, 1)

def canbesplit(items, target, n):
    for l in range(1, len(items) - n + 1):
        for c in (g for g in combinations(items, l) if sum(g) == target):
            if n == 2 and sum(items - set(c)) == target:
                return True
            elif canbesplit(items - set(c), target, n - 1):
                return True
    return False

def solve(items, n):
    hitstarget = lambda g: sum(g) == target
    isvalidsplit = lambda g: canbesplit(set(items) - set(g), target, n - 1)
    target = sum(items) // n
    for l in range(1, len(items)):
        c = combinations(items, l)
        g = sorted(filter(hitstarget, c), key=quantumentanglement)
        for result in g:
            if isvalidsplit(result):
                return quantumentanglement(result)
    return None

def main():
    items = set(map(int, open('24.TXT').read().splitlines()))
    print(solve(items, 3))
    print(solve(items, 4))

if __name__ == '__main__':
    main()


#10723906903
#74850409
