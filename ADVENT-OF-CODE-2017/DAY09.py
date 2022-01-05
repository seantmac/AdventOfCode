test_input = "{{{},{},{{}}}}"
real_input = "9.TXT"

with open(real_input) as f:
    input_data = f.read().strip()


group_count = []
level_tracker = 0
garbage_tracker = False
ignore_next = False
garbage_counter = 0

for this_char in input_data:
    if ignore_next:
        ignore_next = False
    elif this_char == "!":
        ignore_next = True
    else:
        if garbage_tracker:
            if this_char == ">":
                garbage_tracker = False
            else:
                garbage_counter += 1
        elif this_char == "<":
            garbage_tracker = True
        elif this_char == "{":
            try:
                group_count[level_tracker] += 1
            except IndexError:
                group_count.append(1)
            level_tracker += 1
        elif this_char == "}":
            level_tracker -= 1

total_score = 0
level_counter = 0
while True:
    try:
        total_score += (level_counter + 1) * group_count[level_counter]
        level_counter += 1
    except IndexError:
        break

print("Part 1: " + str(total_score))
print("Part 2: " + str(garbage_counter))

#Part 1: 8337
#Part 2: 4330
