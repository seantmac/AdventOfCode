
# file = open("6.TXT")

banks = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

count = 0
seen = {}
while tuple(banks) not in seen:
    seen[tuple(banks)] = count
    i, m = max(enumerate(banks), key=lambda k: (k[1], -k[0]))
    banks[i] = 0
    for j in itertools.islice(itertools.cycle(range(len(banks))), i + 1, i + m + 1):
        banks[j] += 1
    count += 1
print(count)
print(count - seen[tuple(banks)])
