from itertools import combinations
from math import prod


with open('1.TXT', 'r') as f:
    depths = [int(value) for value in f.readlines()]


def count_increments(depths, slice_length):
    increments = 0
    slice_start = 0
    slice_end = slice_start + slice_length
    prev = depths[slice_start:slice_end]
    for i in range(len(depths)):
        idx = i+1
        slice = depths[idx:idx+slice_length]
        if (sum(slice) > sum(prev) and len(slice) == slice_length):
            increments += 1
        prev = slice
    return increments


answer1 = count_increments(depths, 1)
answer2 = count_increments(depths, 3)
print(answer1)
print(answer2)


#1121
#1065