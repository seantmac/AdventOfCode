def solve2():
    data = 'R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, '
    data = data + 'L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, '
    data = data + 'L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, '
    data = data + 'L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, '
    data = data + 'L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2'
    v = (0, 1); x = 0; y = 0
    seen = []
    for item in data:
        l = int("".join(item[1:]))
        v = (v[1], -v[0]) if item[0] == "R" else (-v[1], v[0])
        for ad in range(l):
            x += v[0]
            y += v[1]
            if (x,y) in seen: return (x,y)
            seen.append((x,y))