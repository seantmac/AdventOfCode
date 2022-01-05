firewall = []

with open("13.TXT") as f:
    for line in f:
        this_line = line.strip().split(': ')
        this_line = [int(i) for i in this_line]
        firewall.append(this_line)


def find_position(depth, time):
    position = time % ((depth - 1) * 2)
    if position > (depth - 1):
        position -= ((position - (depth - 1)) * 2)
    return position

severity = 0

for layer in firewall:
    time_visited = layer[0]
    layer_depth = layer[1]
    if find_position(layer_depth, time_visited) == 0:
        severity += layer_depth * time_visited

print("Part 1: " + str(severity))

delay = 1
success = False

while not success:
    success = True
    for layer in firewall:
        time_visited = layer[0] + delay
        layer_depth = layer[1]
        if find_position(layer_depth, time_visited) == 0:
            delay += 1
            success = False
            break

print("Part 2: " + str(delay))
