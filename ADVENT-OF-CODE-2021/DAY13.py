PATH = '13.TXT'
grid = set()
for line in open(PATH):
    if line.startswith('fold'):
        fold = int(line.split('=')[1])
        folded = set()
        for (x, y) in grid:
            y = (2 * fold - y) if 'y' in line and y > fold else y
            x = (2 * fold - x) if 'x' in line and x > fold else x
            folded.add((x, y))
        grid = folded
        print('Active:', len(grid))
    elif line := line.strip():
        grid.add(tuple((int(x) for x in line.split(','))))

for y in range(max([v[1] for v in grid])+1):
    for x in range(max([v[0] for v in grid])+1):
        print('#' if (x, y) in grid else ' ', end='')
    print()

#PART 1:  807
#PART 2:  LGHEGUEJ

# Active: 807
# Active: 675
# Active: 550
# Active: 444
# Active: 374
# Active: 321
# Active: 264
# Active: 220
# Active: 182
# Active: 147
# Active: 118
# Active: 98
# #     ##  #  # ####  ##  #  # ####   ##
# #    #  # #  # #    #  # #  # #       #
# #    #    #### ###  #    #  # ###     #
# #    # ## #  # #    # ## #  # #       #
# #    #  # #  # #    #  # #  # #    #  #
# ####  ### #  # ####  ###  ##  ####  ##

#LGHEGUEJ