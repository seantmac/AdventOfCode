#Generator A starts with 722
#Generator B starts with 354


#Smooth sailing today, except that the code took forever to run, and I forgot how many zeroes
# are in a million so the first time I tried running it I tried 40 billion instead of 40 million.
# Whoops!

#It was also cool how this built on previous puzzles conceptually. Previously I did not know how to
# convert stuff to binary or that XOR was a thing, but those things were in some previous puzzles so
# they immediately came to mind when doing this one, and that made it easy.

previous_a = 722
previous_b = 354

which_part = 2  # Toggle between part 1 and part 2


match_count = 0


def calc_value(previous_value, generator, multiple=1):
    factor_a = 16807
    factor_b = 48271
    divisor = 2147483647

    if generator == "a":
        factor = factor_a
    else:
        factor = factor_b

    while True:
        previous_value = (factor * previous_value) % divisor
        if previous_value % multiple == 0:
            return previous_value


def bin_match(value_1, value_2):
    bin_1 = bin(value_1)[2:].zfill(32)
    bin_1 = int(bin_1[-16:])

    bin_2 = bin(value_2)[2:].zfill(32)
    bin_2 = int(bin_2[-16:])

    if bin_1 ^ bin_2 == 0:
        return True
    return False

if which_part == 1:
    iterations = 40000000
    mult_a = 1
    mult_b = 1
else:
    iterations = 5000000
    mult_a = 4
    mult_b = 8

for i in range(0, iterations):
    previous_a = calc_value(previous_a, "a", multiple=mult_a)
    previous_b = calc_value(previous_b, "b", multiple=mult_b)

    if bin_match(previous_a, previous_b):
        match_count += 1

print("Part " + str(which_part) + ": " + str(match_count))
