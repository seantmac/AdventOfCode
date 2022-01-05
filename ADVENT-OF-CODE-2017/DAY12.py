pipe_list = {}
node_tracker = []
for this_line in open("12.TXT"):
    # Remove the commas, make it into a list, then remove the entry with the <->
    process_line = this_line.strip().replace(",","").split()
    process_line.remove("<->")
    i = 1
    child_list = []

    # Create a list of all but the first entry. These are children of the first entry
    while True:
        try:
            child_list.append(int(process_line[i]))
            i += 1
        except IndexError:
            break

    # Add first: [children] to the dictionary of pipes
    pipe_list.update({int(process_line[0]): child_list})

    # Add the first entry to the list of nodes. We'll use this in part 2
    node_tracker.append(int(process_line[0]))

node_tracker.sort()
connected_list = []     # List to keep track of programs in the group containing program 0. In part 2 we
                        # will add on to this to keep track of programs we've already seen.


def get_connections(pipes, connected, this_program):
    # This function will first check this_program. If it isn't already in the list of programs we've
    # already seen, we will add it. Then it check to see if the children have already been seen. If they
    # haven't, it will call itself on those children. After it finishes, connected will have all of the
    # programs in the group.

    if this_program not in connected:
        connected.append(this_program)
    children = pipes[this_program]
    for this_child in children:
        if this_child not in connected:
            get_connections(pipes, connected_list, this_child)


get_connections(pipe_list, connected_list, 0)
print("Part 1: " + str(len(connected_list)))

group_counter = 1
connected_list.sort()

# Find the first unconnected node. This will be the start of a new group. Then find all its connections
# and add them to the connected list. Continue until we've checked every node.
for this_node in node_tracker:
    if this_node not in connected_list:
        get_connections(pipe_list, connected_list, this_node)
        group_counter += 1

print("Part 2: " + str(group_counter))
