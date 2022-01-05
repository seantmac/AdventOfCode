from itertools import combinations
from math import prod

def part1(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt with f.read 
    ###return "".join(reversed(data))


    with open('01.txt', 'r') as f:
        entries = [int(i) for i in f.read().strip().splitlines()]

    solution = lambda k: next( prod(comb) for comb in combinations(entries, k) if sum(comb) == 2020 )
    return solution(2)
    ##print (solution(2), solution(3))


def part2(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt with f.read 
    ###return "".join(reversed(data))

    with open('01.txt', 'r') as f:
        entries = [int(i) for i in f.read().strip().splitlines()]

    solution = lambda k: next( prod(comb) for comb in combinations(entries, k) if sum(comb) == 2020 )
    return solution(3)
    ##print (solution(2), solution(3))


##Part 1 Output: 1005459
##Part 2 Output: 92643264