import io

with open('AOC2016day02_INPUT.tx') as f:
    # read the input file into lines
    # [[l,i,n,e,1],[l,i,n,e,2]...]
    data = []
    for line in f.readlines():
        data.append(list(line))

#9 8 5 7 5
        
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

location = [1,1]

def press(loc):
    return keypad[loc[0]][loc[1]]

for line in data:
    # line = ['U','U','L','D'...
    for direction in line:
        # direction = 'U'

        # compute new direction
        if direction == 'U':
            location[0] -= 1
        elif direction == 'R':
            location[1] += 1
        elif direction == 'D':
            location[0] += 1
        elif direction == 'L':
            location[1] -= 1

        # check out of bounds
        if location[0] < 0: location[0] = 0
        if location[1] < 0: location[1] = 0
        if location[0] > 2: location[0] = 2
        if location[1] > 2: location[1] = 2

    print(press(location))
