with open('10.TXT', 'r') as f:
    data = [int(line) for line in f]

    # The only possibility is to order all the adapters. Simply count the differences after ordering.
    data.append(0)  # To account for outlet
    data.sort()
    data.append(data[-1] + 3)  # To account for device
    difs = [data[i] - data[i - 1] for i in range(1, len(data))]
    print(f'Part 1: {difs.count(1) * difs.count(3)}')

    # Jolts are not very large, but they are unique: count the number of ways to get to each jolt (adapter),
    # the highest jolt is the device and holds the answer at the end
    ways = [1] * (data[-1] + 1)
    for d in data[1:]:
        ways[d] = sum(ways[n] for n in range(d - 3, d) if n in data)
    print(f'Part 2: {ways[-1]}')

## AOC 2020 Day 10
## Part 1: 2080
## Part 2: 6908379398144
## Loaded puzzle input from 10.txt


#####  Part 1: 2080
#####  Part 2: 6908379398144