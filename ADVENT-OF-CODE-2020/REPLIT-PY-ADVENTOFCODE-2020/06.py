##import functools  (reduce could be part of functools)

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

with open("06.txt", "r") as file:
    data = [x.split('\n') for x in file.read().split('\n\n')]
    print('Part 1: {}'.format(reduce(lambda a,b:a+b, [len(set([v for v in reduce(lambda x,y:x+y, group)])) for group in data])))
    c=0
    for group in data:
        grouped_data = reduce(lambda x,y:x+y, group)
        c += len(set(''.join([x for x in grouped_data if grouped_data.count(x) == len(group)])))
    print('Part 2: {}'.format(c))

## Part 1: 6273
## Part 2: 3254

## AOC 2020 Day 6
## Part 1: 6273
## Part 2: 3254