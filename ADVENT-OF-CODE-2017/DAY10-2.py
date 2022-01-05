#Now for part 2. I had to read it 4 or 5 times to really understand what it was asking
# of me. There's a part where you have a list of 256 things, and you have to take chunks
# of 16 elements, and XOR them together, to get 16 total results (since 16 x 16 = 256).
# It took me a while to figure out how I would make that loop work, and then I did it
# wrong, so I spent a while debugging it. My error was in line 35. I had
# this_hash = list_elements[i] instead of the correct
# this_hash = list_elements[i * 16]. So for example instead of XOR'ing elements
# 16 thru 31 together, I was XOR'ing element 1 with elements 17-31.

puzzle_input = "199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192"

list_elements = []
list_size = 256
for i in range(0, list_size):
    list_elements.append(i)

current_position = 0
skip_size = 0

puzzle_sequence = []

for this_char in puzzle_input:
    puzzle_sequence.append(ord(this_char))  # ord(char) gives the ASCII number

puzzle_sequence.extend((17, 31, 73, 47, 23))

for i in range(0, 64):  # This is the same code from part 1, just done 64 times
    for this_length in puzzle_sequence:
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

dense_hash = []

for i in range(0, 16):  # Here we do XOR to 16 chunks of 16 numbers
    this_hash = list_elements[i * 16]
    for n in range(1, 16):
        this_hash = this_hash ^ list_elements[16 * i + n]
    dense_hash.append(this_hash)

knot_hash = ""

for this_entry in dense_hash:
    knot_hash += str(hex(this_entry))[-2:]

print("Part 2: " + knot_hash)
