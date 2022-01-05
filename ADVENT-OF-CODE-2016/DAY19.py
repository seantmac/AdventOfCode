#3017957
#!/usr/bin/env python
import collections


def process_p1(n):
    elves = collections.deque(range(1, n + 1))
    while len(elves) > 1:
        elves.rotate(-1)
        elves.popleft()

    return elves.popleft()


def process_p2(n):
    elves = collections.deque(range(1, n + 1))
    eleft = len(elves)

    # use coff to remember how far we are rotated from the "current" elf
    # instead of rotating back to the next position (turns out to be *incredibly* slow),
    # we'll just calculate this value into the next rotation
    coff = 0

    while eleft > 1:
        n = (eleft // 2) - coff
        elves.rotate(-n)
        elves.popleft()
        eleft -= 1
        coff = (coff + n - 1) % eleft

    return elves.popleft()


if __name__ == '__main__':
    with open('19.TXT') as inf:
        ecount = int(inf.read().strip())

    print('== part 1 ==')
    elf = process_p1(ecount)
    print('Elf #{} has the presents\n'.format(elf))

    print('== part 2 ==')
    elf = process_p2(ecount)
    print('Elf #{} has the presents\n'.format(elf))