#cartesian product to get 2 and 3 char unique codes

import itertools
import string

chars = itertools.product(string.digits +string.ascii_uppercase, repeat = 3)
#spin cartesian product of 0-9 and A-Z, all 36 chars, to gen all 3 character combo's

outfileA = open("alpha3.txt", "w")
for line in chars:
    # write line to output file
    line = ''.join(line)
    outfileA.write(line)
    outfileA.write("\n")
outfileA.close()


chars = itertools.product(string.digits +string.ascii_uppercase, repeat = 2)
#spin cartesian product of 0-9 and A-Z, all 36 chars, to gen all 3 character combo's

outfileA = open("alpha2.txt", "w")
for line in chars:
    # write line to output file
    line = ''.join(line)
    outfileA.write(line)
    outfileA.write("\n")
outfileA.close()


for c in chars:
    sent_str = ''.join(c)
    print (sent_str)