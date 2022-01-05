with open('11.TXT', 'r') as f:
    grid = [[int(i) for i in line] for line in f.read().split('\n')]


def flash_wave(r, c):
    flashed = []
    for i, j in ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1),
                 (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)):
        if 0 <= i < 10 and 0 <= j < 10 and grid[i][j] != 10:
            grid[i][j] += 1
            if grid[i][j] == 10:
                flashed.append((i, j))
    return flashed


def AOC_day11_pt1_and_pt2():
    total_flashes = 0
    steps = 0

    while True:
        flashed = []
        for r in range(10):
            for c in range(10):
                grid[r][c] += 1
                if grid[r][c] == 10:
                    flashed.append((r, c))
        for (r, c) in flashed:
            flashed += flash_wave(r, c)
        total_flashes += len(flashed)
        steps += 1

        if steps == 100:
            pt1_flashes = total_flashes

        if all(sum(row) == 100 for row in grid):
            return pt1_flashes, steps
        for r, c in flashed:
            grid[r][c] = 0


flashes_after_100_steps, steps_until_synced = AOC_day11_pt1_and_pt2()


def AOC_day11_pt1():
    return flashes_after_100_steps


def AOC_day11_pt2():
    return steps_until_synced


print(AOC_day11_pt1())
print(AOC_day11_pt2())

#1625
#244