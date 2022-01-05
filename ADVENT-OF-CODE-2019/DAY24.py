def neighbors(pos):
    x, y = pos
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


def rneighbors(pos):
    x, y, z = pos
    if x < 4 and not (x == 1 and y == 2):
        yield x + 1, y, z
    if x > 0 and not (x == 3 and y == 2):
        yield x - 1, y, z
    if y < 4 and not (x == 2 and y == 1):
        yield x, y + 1, z
    if y > 0 and not (x == 2 and y == 3):
        yield x, y - 1, z
    if y == 2:
        if x == 1:
            yield from ((0, y, z + 1) for y in range(5))
        if x == 3:
            yield from ((4, y, z + 1) for y in range(5))
    if x == 2:
        if y == 1:
            yield from ((x, 0, z + 1) for x in range(5))
        if y == 3:
            yield from ((x, 4, z + 1) for x in range(5))
    if x == 4:
        yield (3, 2, z - 1)
    if x == 0:
        yield (1, 2, z - 1)
    if y == 4:
        yield (2, 3, z - 1)
    if y == 0:
        yield (2, 1, z - 1)


def rules(field, pos):
    friends = sum(field[neigh] for neigh in neighbors(pos) if neigh in field)
    if field[pos]:
        return friends == 1
    else:
        return 1 <= friends <= 2


def rrules(field, pos):
    friends = sum(neigh in field for neigh in rneighbors(pos))
    if pos in field:
        return friends == 1
    else:
        return 1 <= friends <= 2


def evolve(field):
    return {pos: rules(field, pos) for pos in field}


def revolve(field):
    _, _, zmax = map(max, zip(*field))
    _, _, zmin = map(min, zip(*field))
    spaces = ((x, y, z) for x in range(5) for y in range(5) for z in range(zmin - 1, zmax + 2) if not (x == y == 2))
    return {pos for pos in spaces if rrules(field, pos)}


def biodiversity(field):
    return sum(alive << (5 * y + x) for (x, y), alive in field.items())


def display(field):
    for y in range(5):
        print("".join(".#"[field[x, y]] for x in range(5)))


def rdisplay(field):
    _, _, zmax = map(max, zip(*field))
    _, _, zmin = map(min, zip(*field))
    for z in range(zmin, zmax + 1):
        print("\ndepth:", z)
        for y in range(5):
            print("".join(".#"[(x, y, z) in field] for x in range(5)))


data = """\
.###.
..#.#
...##
#.###
..#..
"""

example = """\
....#
#..#.
#..##
..#..
#...."""


def part1():
    field = {(x, y): cell == "#" for y, row in enumerate(data.splitlines()) for x, cell in enumerate(row)}
    seen = {biodiversity(field)}
    for attempt in range(10000):
        field = evolve(field)
        hashed = biodiversity(field)
        if hashed in seen:
            print(hashed)
            break
        seen.add(hashed)


def part2():
    field = {(x, y, 0) for y, row in enumerate(data.splitlines()) for x, cell in enumerate(row) if cell == "#"}
    for attempt in range(200):
        field = revolve(field)
    print(len(field))


if __name__ == '__main__':
    part1()
    part2()

#27562081
#1893