#This one went pretty smoothly for me. I got tripped up for a while on a bug; when I was
# changing direction I was telling it to go the wrong way in the case of an IndexError
# exception. But once I got that, everything was good. I am kind of curious to see what
# possible solution there would be that doesn't make part 2 a matter of adding a counter.


###   ALL THANKS TO https://www.reddit.com/user/hugseverycat   ###
###   thank you, Denise

routing_diagram = []

with open("19.TXT") as f:
    for this_line in f:
        diagram_row = []
        for character in this_line:
            if character != '\n':
                diagram_row.append(character)
        routing_diagram.append(diagram_row)

current_row = 0
current_col = 0
step_counter = 0
path_completed = False
letters_found = ""
current_direction = 'down'

diagram_width = len(routing_diagram[current_row])
diagram_height = len(routing_diagram)


for col in range(0, diagram_width):
    if routing_diagram[current_row][col] == '|':
        current_col = col
        break

while not path_completed:
    try:
        current_path_char = routing_diagram[current_row][current_col]
    except IndexError:
        print("Row: " + str(current_row))
        print("Col: " + str(current_col))
        raise
    if current_path_char == " ":
        path_completed = True
        break
    elif current_row > diagram_height or current_col > diagram_width:
        path_completed = True
        break
    elif current_path_char.isalpha():
        letters_found += current_path_char
    elif current_path_char == '+':  # Change direction
        if current_direction == 'right' or current_direction == 'left':
            try:
                if routing_diagram[current_row + 1][current_col] == ' ':
                    current_direction = 'up'
                else:
                    current_direction = 'down'
            except IndexError:
                current_direction = 'up'
        else:
            try:
                if routing_diagram[current_row][current_col + 1] == ' ':
                    current_direction = 'left'
                else:
                    current_direction = 'right'
            except IndexError:
                current_direction = 'left'

    if current_direction == 'down':
        current_row += 1
    elif current_direction == 'up':
        current_row -= 1
    elif current_direction == 'right':
        current_col += 1
    elif current_direction == 'left':
        current_col -= 1
    else:
        print("Invalid direction: " + str(current_direction))
    step_counter += 1

print("Part 1: DOES NOT WORK " + str(letters_found))
print("Part 2: " + str(step_counter))
