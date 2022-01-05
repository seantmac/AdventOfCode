#Not my best work, to be honest. The code below looks nice, but it's not really from me. I got part 1 just fine
# (with much less nice looking code), but part 2 eluded me. I tried brute-forcing it, then when it took a long
# time, spent the better part of the day trying to think of mathy solutions, and failed. Then I checked the
# solutions thread and saw that some people were brute forcing it with a more optimized use of deque than I was
# using so I tightened it up a bit and was able to brute force the part 2 solution. So yeah, I had to "cheat"
# some with this one. Grumble.

###   ALL THANKS TO https://www.reddit.com/user/hugseverycat   ###

from collections import deque

input_value = 380
#335

buffer = deque([0])

for position in range(1, 2018):
    buffer.rotate(-input_value)
    buffer.append(position)

print("Part 1: " + str(buffer[0]))

for position in range(2018, 50000000):
    buffer.rotate(-input_value)
    buffer.append(position)

print("Part 2: " + str(buffer[buffer.index(0) + 1]))

#Part 1: 204
#Part 2: 28954211
