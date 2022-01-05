#UGH. So I wrote this recursive thingie, but it kept giving me a max recursion error.
# So then I tried to make it non recursive and that failed horribly. I tried increasing
# the max recursion and I got the wrong answer. I was seriously about to give up.

#Then I re-read the question and realized that I'm NOT supposed to count diagonals as adjacents.

#So then I made the proper adjustment to the valid "neighbors" and got the right answer.
# ARGH!! Read more carefully next time Denise :-)



###   ALL THANKS TO https://www.reddit.com/user/hugseverycat   ###
#"ljoxqyyw"  hugseverycat's input, different from mine



def get_knot_hash(puzzle_input):
    # This is from day 10
    list_elements = []
    list_size = 256
    for knot_counter in range(0, list_size):
        list_elements.append(knot_counter)

    current_position = 0
    skip_size = 0

    puzzle_sequence = []

    for this_char in puzzle_input:
        puzzle_sequence.append(ord(this_char))  # ord(char) gives the ASCII number

    puzzle_sequence.extend((17, 31, 73, 47, 23))

    for knot_counter in range(0, 64):  # This is the same code from part 1, just done 64 times
        for this_length in puzzle_sequence:
            temp_list = []
            for kc in range(current_position, current_position + this_length):
                temp_list.append(list_elements[kc % list_size])
            temp_list.reverse()
            temp_index = 0
            for kc in range(current_position, current_position + this_length):
                list_elements[kc % list_size] = temp_list[temp_index]
                temp_index += 1

            current_position = (current_position + this_length + skip_size) % list_size
            skip_size += 1

    dense_hash = []

    for knot_counter in range(0, 16):  # Here we do XOR to 16 chunks of 16 numbers
        kc_hash = list_elements[knot_counter * 16]
        for n in range(1, 16):
            kc_hash = kc_hash ^ list_elements[16 * knot_counter + n]
        dense_hash.append(kc_hash)

    knot_hash = ""

    for this_entry in dense_hash:
        this_hex = str(hex(this_entry)).ljust(4, "0")[-2:]
        knot_hash += this_hex

    return knot_hash


def get_binary(puzzle_char):
    puzzle_char = str(puzzle_char)  # Just in case it's an integer
    scale = 16
    bits = 4
    try:
        return bin(int(puzzle_char, scale))[2:].zfill(bits)
        # zfill adds leading zeroes if necessary

def count_used(binary_string):
    used_counter = 0
    for this_char in binary_string:
        if this_char == "1":
            used_counter += 1
    return used_counter

puzzle_grid = []

def do_part_1():
    my_input = "oundnydw"

    used = 0
    for i in range(0, 128):
        this_input = my_input + "-" + str(i)
        this_hash = get_knot_hash(this_input)
        this_binary = ""
        for each_char in this_hash:
            this_binary += get_binary(each_char)
        puzzle_grid.append(this_binary)
        used += count_used(this_binary)

    print("Part 1: " + str(used))
    return used


def do_part_2():
    visited_grid = [([0] * 128) for i in range(128)]
    island_count = 0

    with open("14.TXT") as f:  # I saved the grid created by my input since part 1 takes forever to run
        for line in f:
            puzzle_grid.append(tuple(line.strip().split(',')))


    def mark_visited(check_row, check_col):
        visited_grid[check_row][check_col] = True

    def is_in_island(check_row, check_col):
        if check_row in range(0, 128) and check_col in range(0, 128):
            if not visited_grid[check_row][check_col] and puzzle_grid[check_row][check_col] == "1":
                return True
        return False

    def get_connections(check_row, check_col):
        mark_visited(check_row, check_col)
        neighbor_rows = (-1,  0, 0, 1)
        neighbor_cols = ( 0, -1, 1, 0)
        for n in range(0, 4):
            n_row = check_row - neighbor_rows[n]
            n_col = check_col - neighbor_cols[n]
            if is_in_island(n_row, n_col):
                get_connections(n_row, n_col)

    for row in range(0, 128):
        for col in range(0, 128):
            if not visited_grid[row][col] and puzzle_grid[row][col] == "1":
                island_count += 1
                get_connections(row, col)

    print("Part 2 (but with wrong answer): " + str(island_count))

do_part_1()
do_part_2()

#Part 1: 8106
#Part 2: 1157  WRONG  It is 1164
