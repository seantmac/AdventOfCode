#! /usr/bin/env python3


def puzzle(list):
    index = 0
    steps = 0
    while index >= 0 and index < len(list):
        value = list[index]
        if value >= 3:
            list[index] -= 1
        else:
            list[index] += 1
        index += value
        steps += 1
    print(steps)
    return steps



if __name__ == '__main__':
    list = list(map(int, input('5.TXT').split('\n')))
    solution(puzzle(list))
