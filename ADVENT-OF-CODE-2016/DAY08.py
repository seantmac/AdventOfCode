# -*- coding: utf-8 -*-
import re
import numpy as np

screen = np.array(['.'] * (50 * 6)).reshape(6, 50)

for line in open(r'8.TXT'):
    sline = line.strip()
    re_rect = re.search(r'rect (\d+)x(\d+)', sline)
    re_rotate = re.search(r'rotate (column|row) (x|y)=(\d+) by (\d+)', sline)

    if re_rect:
        width, height = map(int, re_rect.group(1, 2))
        screen[:height, :width] = '#'
    elif re_rotate:
        what, [index, shift] = re_rotate.group(1), map(int, re_rotate.group(3, 4))
        if what == 'column':
            shift %= 6
            screen[:, index] = np.hstack((screen[-shift:, index], screen[:-shift, index]))
        elif what == 'row':
            shift %= 50
            screen[index] = np.hstack((screen[index, -shift:], screen[index, :-shift]))

print('Part 1:', screen[(screen == '#')].size)
print('Part 2:')

for screen_line in screen.tolist():
    print(''.join(screen_line))


##  Part 1: 128
##  Part 2:  EOARGPHYAO
####..##...##..###...##..###..#..#.#...#.##...##..
#....#..#.#..#.#..#.#..#.#..#.#..#.#...##..#.#..#.
###..#..#.#..#.#..#.#....#..#.####..#.#.#..#.#..#.
#....#..#.####.###..#.##.###..#..#...#..####.#..#.
#....#..#.#..#.#.#..#..#.#....#..#...#..#..#.#..#.
####..##..#..#.#..#..###.#....#..#...#..#..#..##..