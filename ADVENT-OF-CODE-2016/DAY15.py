disks = []
for line in open("15.TXT", "r").read().strip().split("\n"):
    args = line.split()
    disks.append((int(args[3]), int(args[-1][:-1])))

# Part 2
# disks.append((11, 0))

time = 0
while sum((y + time + t) % x for t, (x, y) in enumerate(disks, 1)) != 0:
    time += 1

print(time)

##INPUT
'''
Disc #1 has 17 positions; at time=0, it is at position 15.
Disc #2 has 3 positions; at time=0, it is at position 2.
Disc #3 has 19 positions; at time=0, it is at position 4.
Disc #4 has 13 positions; at time=0, it is at position 2.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 5 positions; at time=0, it is at position 0.
'''

#Part 1   400589
#Part 2  3045959
