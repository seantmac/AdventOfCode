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
                name = str(word)
            elif(count == 1):
                weights[name] = int(word.strip('()'))
            else:
                if(len(word) is not 2):
                    hold.add(word.strip(','))

            count += 1
        if(len(hold) > 0):
            holding[name] = hold

#---------------Solution 2--------------#
# http://adventofcode.com/2017/day/7

def totalWeight(label):
    totW = 0

    subs = {}
    for sub in holding[label]:
        if(sub in holding):
            subs[sub] = totalWeight(sub)
        else:
            subs[sub] = weights[sub]

    x = 0
    s = next(iter(subs))
    w = subs[s]
    for s_ in subs:
        if(subs[s_] is not w):
            x += subs[s_] - w
            if (x is not 0):
                subs[s_] -= x
                weights[s_] -= x
                print("Part two:", weights[s_])

    for s in subs:
        totW += subs[s]
    totW += weights[label]

    return totW

#---------------------------------------#
totalWeight('bpvhwhh')


# input function is the solution of part one, in my case 'bpvhwhh'

#! It is possible that you need to run it a few times,
#                       until it gives only one solution
# Correct answer:
