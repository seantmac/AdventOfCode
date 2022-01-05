# Enormous thanks to this site, without which I would have been totally lost in the woods
# http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/

with open("11.TXT") as f:
    process_path = f.read().strip().split(",")

current_coord = [0, 0]
max_distance = 0


def take_step(coord, step_direction):
    x = coord[0]
    y = coord[1]

    if step_direction == "n":
        y += 1
    elif step_direction == "ne":
        x += 1
    elif step_direction == "se":
        x += 1
        y -= 1
    elif step_direction == "s":
        y -= 1
    elif step_direction == "sw":
        x -= 1
    else:  # step_direction == "nw"
        x -= 1
        y += 1

    return [x, y]


def find_depth_from_coord(x, y):
    z = -(x + y)
    return max(abs(x), abs(y), abs(z))


for this_step in process_path:
    current_coord = take_step(current_coord, this_step)
    current_distance = find_depth_from_coord(current_coord[0], current_coord[1])
    if current_distance > max_distance:
        max_distance = current_distance

print("Part 1: " + str(current_distance))
print("Part 2: " + str(max_distance))
