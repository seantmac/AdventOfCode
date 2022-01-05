#I decided to write this one in two separate files.
# The code wasn't that different between parts 1 and 2,
# but the way it was used was.

#Part 1 is first, part 2 down below. I did not have too much trouble with part 1.
# As with yesterday though, I was really unsure of my approach so it took me a
# while simply because I meticulously tested everything as I went.

real_input = "199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192"
test_input = "3,4,1,5"
list_elements = []
test_list = [0, 1, 2, 3, 4]

which_input = real_input    # Toggle whether we're using real or test input

if which_input == real_input:   # Create the list
    for i in range(0, 256):
        list_elements.append(i)
else:
    list_elements = test_list

which_input = [int(x) for x in which_input.split(",")]  # Turn the input into a list of integers
list_size = len(list_elements)

skip_size = 0
current_position = 0

for this_length in which_input:
    temp_list = []
    for i in range(current_position, current_position + this_length):
        temp_list.append(list_elements[i % list_size])
    temp_list.reverse()
    temp_index = 0
    for i in range(current_position, current_position + this_length):
        list_elements[i % list_size] = temp_list[temp_index]
        temp_index += 1

    current_position = (current_position + this_length + skip_size) % list_size
    skip_size += 1

print("Part 1: " + str(list_elements[0] * list_elements[1]))
