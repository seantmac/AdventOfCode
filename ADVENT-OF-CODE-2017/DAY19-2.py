def solve(graph):
    steps = 0
    direction = [1, 0]
    y = 0
    x = 0
    while graph[y][x] != '|':
        x += 1

    while True:
        if y < 0 or y >= len(graph) or x < 0 or x >= len(graph[0]) or graph[y][x] == ' ':
            return steps

        steps += 1
        ny = y + direction[0]
        nx = x + direction[1]

        if graph[y][x] == '+':
            if direction[0] != 0:
                ny = y
                if x > 0 and graph[y][x - 1] == '-':
                    direction = [0, -1]
                    nx = x - 1
                else:
                    direction = [0, 1]
                    nx = x + 1
            else:
                nx = x
                if y > 0 and graph[y - 1][x] == '|':
                    direction = [-1, 0]
                    ny = y - 1
                else:
                    direction = [1, 0]
                    ny = y + 1

        y = ny
        x = nx

with open('19.TXT', 'r') as f:
    graph = [line for line in f]
    print("THE ANSWER TO PART i IS:   ", str(solve(graph)))

