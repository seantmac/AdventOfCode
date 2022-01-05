def answer(parttwo):
    jumps = list(map(int,[x.rstrip() for x in open('5.TXT','r').readlines()]))
    jump = 0
    s = 0
    while jump < len(jumps) and jump >= 0:
        j = jumps[jump]
        if j >= 3 and parttwo:
            jumps[jump] -= 1
        else:
            jumps[jump] += 1
        jump += j
        s += 1
    print(s)
answer(0)
answer(1)

#376976
