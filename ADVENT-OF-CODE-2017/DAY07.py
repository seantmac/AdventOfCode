#------------------Day7-----------------#
#------------------Info-----------------#
# Event:    Advent of Code
# Year:     2017
# Source:   http://adventofcode.com/
# Maker:    Eric Wastl
# URL:      http://was.tl/

# Solved by Quint Daenen
# URL:      http://quint.ulyssis.be/

# This is not the one and only solution,
# and certainly not the best. It is just
# the way I solved it at the time.

#--------------Import Data--------------#
# http://adventofcode.com/2017/day/7/input
holding = {}
weights = {}
with open('7.TXT','r') as f:
    for line in f:
        count = 0
        hold = set()
        for word in line.split():
            if(count == 0):
                name = word
            elif(count == 1):
                weights[name] = int(word.strip('()'))
            else:
                if(len(word) is not 2):
                    hold.add(word.strip(','))

            count += 1
        if(len(hold) > 0):
            holding[name] = hold

#---------------Solution 1--------------#
# http://adventofcode.com/2017/day/7
name = ""

for x in holding.keys():
    found = False
    for y in holding.values():
        if x in y:
            found = True
            break

    if not found:
        name = x
        break

# ---------------------------------------#
print("Part one: %s" % name)

# Correct answer:  bpvhwhh
