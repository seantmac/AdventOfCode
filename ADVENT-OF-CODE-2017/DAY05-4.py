lines = [line.strip() for line in open('5.TXT', 'r').readlines()]

jumps = [int(x) for x in lines]
n = len(jumps)
curr = 0
count = 0

while curr >= 0 and curr < n:
    jumps[curr] += 1
    curr += jumps[curr] - 1
    count += 1

print("PART 1 IS   " , count)
#PART 1 IS    376976


jumps = [int(x) for x in lines]
n = len(jumps)
curr = 0
count = 0

while curr >= 0 and curr < n:
    prev = jumps[curr]
    jumps[curr] += 1 if prev < 3 else -1
    curr += prev
    count += 1

print("PART 2 IS   " , count)
#PART 2 IS    29227751
