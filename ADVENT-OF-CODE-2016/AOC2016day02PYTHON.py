import io

digits = []

filein = open ('AOC2016day02_INPUT.tx', 'r')

for line in filein:
    digits.append(line)

keypad = {(-1,1):2, (0,1):3, (1,1):4, (-1,0):6, (0,0):7, (1,0):8, (-1,-1):'A', (0,-1):'B', (1,-1):'C', (2,0):9, (-2,0):5, (0,-2):'D', (0,2):1}

#
#C D 8 D 4


numbers = []

for digit in digits:
    finger_x = -2
    finger_y = 0

    for move in digit:
        if move == 'U':
            finger_y +=1
            coord = (finger_x, finger_y)
            try:
                keypad[coord]
            except KeyError:
                #print('up')
                finger_y -=1
                continue
        if move == 'D':
            finger_y -=1
            coord = (finger_x, finger_y)
            try:
                keypad[coord]
            except KeyError:
                #print('down')
                finger_y +=1
                continue
        if move == 'L':
            finger_x-=1
            coord = (finger_x, finger_y)
            try:
                keypad[coord]
            except KeyError:
                #print('left')
                finger_x +=1
                continue
        if move == 'R':
            finger_x +=1
            coord = (finger_x, finger_y)
            try:
                keypad[coord]
            except KeyError:
                #print('right')
                finger_x -=1
                continue

        press = keypad[(finger_x, finger_y)]
    print(press)
