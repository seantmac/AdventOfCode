## Python 3, for part 1 just replace 2016 with 0

from hashlib import md5
from sys import exit, setrecursionlimit
setrecursionlimit(10000)

salt = 'ihaygndm'
i = 0
hashes = []
triplets = []
quintuplets = []
keys = []

def hash(input, stretching):
    if stretching > 0:
        return hash(md5(input.encode('ascii')).hexdigest(), stretching-1)
    else:
        return md5(input.encode('ascii')).hexdigest()

while i < 50000:
    hashes.append(hash(salt+str(i), 0))
    for c in range(30):
        char = hashes[i][c]
        if hashes[i][c:c+3] == char*3:
            triplets.append((i,char))
            print('found triplet', char, i, len(triplets))
            if hashes[i][c:c+5] == char*5:
                quintuplets.append((i,char))
                print('found quintuplet', char, i, len(quintuplets))
            break
    i+=1

for triplet in triplets:
    if len([i for (i,char) in quintuplets if triplet[0] < i <= triplet[0]+1000 and char == triplet[1]]) > 0:
        keys.append(triplet)
        print('found key', triplet, len(keys))
        if len(keys) == 64:
            print('64th key', triplet)
            exit()

# 1   64th key (15035, '0')
# 2   64th key (19968, 'e')64th key (19968, 'e')
