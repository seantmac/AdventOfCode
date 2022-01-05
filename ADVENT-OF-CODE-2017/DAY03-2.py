"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8 3^2  10
21  22  23  24 5^2
..  ..  ..  ..  .. 7^2
"""

import math

input = 277678

def side_length(number):
    side = math.ceil(math.sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side

side = side_length(input)
steps_to_reach_center_from_axis = (side-1)/2
axises = [side**2 - ((side-1) * i)  - math.floor(side/2) for i in range(0, 4)] #get the axis "cells"
steps_to_reach_axix_from_input = min([abs(axis - input) for axis in axises])

print(steps_to_reach_axix_from_input + steps_to_reach_center_from_axis)

#part1
#475.0

#part2
# is just go here and pick the one from the integer sequence since it is listed/defined here
# https://oeis.org/A141481/b141481.txt
# https://oeis.org/A141481
# http://oeisf.org/
# 279138
