from collections import defaultdict


def walk(room: str, path: list) -> list:
    path.append(room)

    if 'end' in path:
        paths.append(path)
        return path

    for r in rmap[room]:
        if r.islower() and r in path:
            continue

        # recursion
        # pass by reference pass by value make a list() or you'll be sorry
        walk(r, list(path))


itxt = [i.split('-') for i in open("12.TXT", mode='r').read().split()]
rmap = {a: {b} for a, b in itxt}
rmap.update({b: {a} for a, b in itxt})

for a, b in itxt:
    rmap[a].add(b)
    rmap[b].add(a)

paths = list()

path = walk('start', [])

print("pt1:", len(paths))


def passage_pathing(cave_map):
    # Recursive depth-first search
    def dfs(cave_map, visited, loc, visited_small):

        # Keep track of which nodes have been visited and how many times
        # If just doing part 1, you only need to add the visited node to
        # the dict or use a set instead
        new_visited = visited.copy()
        if loc == "end":
            return 1
        if loc in new_visited:
            new_visited[loc] += 1
        else:
            new_visited[loc] = 1

        # For every node that the current location points to...
        # If going to an upper case node, just go, no worries
        # If going to a lower case node, make sure it's not visited already
        paths = 0
        for to in cave_map[loc]:
            if to.isupper():
                paths += dfs(cave_map, new_visited, to, visited_small)
            elif to not in new_visited:
                paths += dfs(cave_map, new_visited, to, visited_small)
            # For part 2 you can also go to a lower case node if you haven't been
            # twice already or to another node twice
            elif to in new_visited and new_visited[to] < 2 and not visited_small:
                paths += dfs(cave_map, new_visited, to, True)

        return paths

    visited = {}
    return dfs(cave_map, visited, "start", False)


if __name__ == "__main__":
    cave_map = defaultdict(list)
    with open('12.TXT', 'r') as input:
        for line in input:
            connection = line.rstrip().split("-")

            # Create a map of every left node to every right node an vise versa
            # If one of the nodes is start, only keep track of what start goes to
            # Similarly if one node is end, only keep track of what goes to end
            if connection[1] != "start" and connection[0] != "end":
                cave_map[connection[0]].append(connection[1])
            if connection[0] != "start" and connection[1] != "end":
                cave_map[connection[1]].append(connection[0])

    print(passage_pathing(cave_map))   #PART2

#pt1: 4186      YUP
#PART2:92111    YUP!

#part1: 2507  nope  Part 1: 2507  nope
#part2: 50246
#Part 2: 48063