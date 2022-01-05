def move(lines, start_coordinate, start_line, tree, across, down):
    '''take in a ski slope represented by a nested list.  Move by whatever    coordinates you like. Return tress and other variables for repeated calling'''

    if len(lines) > start_line + down:
        if len(lines[start_line + down]) > start_coordinate + across:
            end_line = lines[start_line + down][start_coordinate + across]
            if end_line == '#':
                tree += 1
            return (lines, start_coordinate + across, start_line + down, tree)
        else:
            return ('beyond slope width')
    else:
        return ('beyond slope height')


def extend_list(lines, line_index_current):
    '''the list is not long enough to get to the bottom.
    When you run out of list i.e. you need to go sideways but can't:
    i) extend remaining list objects by 2 times (2 is arbritrary)
    ii) delete original list entires that are getting multiplied
    iii) add truncated list and list with multiplied objcts together.'''

    indexes = list(range(line_index_current, len(lines)))
    temp_list = [lines[line_index].replace('\n', '') * 2 for line_index in indexes]
    lines = lines[0:line_index_current]
    return lines + temp_list


def find_slope(lines, across, down):
    tree = 0
    start_coordinate = 0
    start_line = 0
    for line_index in range(len(lines)):

        # if start_line+down <= len(lines), you are beyond slope
        if start_line + down < len(lines):
            temp_outer = move(lines, start_coordinate, start_line, tree, across, down)
            if type(temp_outer) != str:

                # update parameters
                tree = temp_outer[3]
                start_coordinate = temp_outer[1]
                start_line = temp_outer[2]

            # else if move doesnt work
            else:
                if temp_outer == 'beyond slope width':

                    # fatten the slope
                    lines = extend_list(lines, line_index)

                    # repeat the above
                    temp_inner = move(lines, start_coordinate, start_line, tree, across, down)
                    if type(temp_inner) != str:
                        tree = temp_inner[3]
                        start_coordinate = temp_inner[1]
                        start_line = temp_inner[2]

                    # should not get printed:
                    else:
                        print('bad width logic')
                        break

                # should not get printed:
                elif temp_outer == 'beyond slope height':
                    print('bad height logic')
                    break

                # should not get printed:
                else:
                    print('unexpected logic')
                    break
    return tree


with open('3.TXT', 'r') as infile:
    # make list of 'line' strings
    lines_raw = infile.readlines()
    lines = [line.replace('\n', '') for line in lines_raw]

test1 = find_slope(lines, 1, 1)
test2 = find_slope(lines, 3, 1)
test3 = find_slope(lines, 5, 1)
test4 = find_slope(lines, 7, 1)
test5 = find_slope(lines, 1, 2)

Part1 = test2
Part2 = test1 * test2 * test3 * test4 * test5

print('Part1:  ', Part1)
print('Part2:  ', Part2)

## Part1:   278
## Part2:   9709761600
