import re

with open("02.txt") as raw_data:
    data = raw_data.readlines()
arr = []
regex = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>.):\s(?P<password>.*)$')

for item in data:
    arr.extend([match.groupdict() for match in regex.finditer(item)])

def part1():
    count = 0
    for item in arr:
        char_count = item["password"].count(item["char"])
        if int(item["min"]) <= char_count <= int(item["max"]):
            count += 1
    return count

def part2():
    count = 0
    for item in arr:
        pos1, pos2 = int(item["min"]) - 1, int(item["max"]) - 1
        cond = sorted((item["password"][pos1] == item["char"], item["password"][pos2] == item["char"]))
        if cond == [False, True]:
            count += 1
    return count

print(f"Day 2.1: {part1()}")
print(f"Day 2.2: {part2()}")

##Day 2.1: 556
##Day 2.2: 605