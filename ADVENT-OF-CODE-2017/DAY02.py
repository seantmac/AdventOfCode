#!/usr/bin/python
import itertools
def even_divisors(rows):
    for row in rows:
        for a, b in itertools.combinations(sorted(row), 2):
            if b % a == 0:
                yield a, b

def digits(filehandle):
    for line in filehandle:
        if line.strip():
            yield list(map(int, line.split()))

with open("2.txt") as f:
    checksum = sum(b-a for a, *_, b in map(sorted, digits(f)))
    print(checksum)

with open("2.txt") as f:
    checksum = sum(b//a for a, b in even_divisors(digits(f)))
    print(checksum)

#48357
#351
