from collections import deque

scores1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores2 = {")": 1, "]": 2, "}": 3, ">": 4}
tbl = {"(": ")", "[": "]", "{": "}", "<": ">"}

with open("10.TXT", 'r') as f:
    data = list(map(lambda x: x.strip(), f.readlines()))


# Part 1

def parse_brackets_score(data: list[str]) -> int:
    total = 0
    for line in data:
        q = deque()
        for p in line:
            if p in scores1.keys():
                val = q.pop()
                if tbl[val] != p:
                    total += scores1[p]
                    break
            else:
                q.append(p)
    return total


print(parse_brackets_score(data))


# Part 2

def complete_brackets_score(data: list[str]):
    totals = []
    for line in data:
        total = 0
        q = deque()
        for idx, p in enumerate(line):
            n = len(line) - 1
            if p in scores2.keys():
                val = q.pop()
                if tbl[val] != p:
                    break
            else:
                q.append(p)
            if idx == n:
                while q:
                    total = total * 5 + scores2[tbl[q.pop()]]
                totals.append(total)
    return sorted(totals)[len(totals) // 2]


print(complete_brackets_score(data))

#268845
#4038824534