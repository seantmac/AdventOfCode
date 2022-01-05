#I had a lot of trouble with part 2 of this one. I was on the right track but must have been doing the
# wrong mod operation. And since we didn't have any sample solutions I kept putting in the wrong answer.
# This morning I woke up with the brilliant idea that I could work on making my code work for 100 cycles,
# and if I did that, it would work for a billion too. And it did. Yay!

###   ALL THANKS TO https://www.reddit.com/user/hugseverycat   ###

from collections import deque

with open("16.TXT") as f:
    dance_moves = f.read().strip().split(',')

start_positions = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
dancing_programs = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])


def spin(x, dancers):
    dancers.rotate(x)


def exchange(pos_a, pos_b, dancers):
    letter_a = dancers[pos_a]
    letter_b = dancers[pos_b]
    dancers[pos_a] = letter_b
    dancers[pos_b] = letter_a


def partner(letter_a, letter_b, dancers):
    pos_a = dancers.index(letter_a)
    pos_b = dancers.index(letter_b)
    dancers[pos_a] = letter_b
    dancers[pos_b] = letter_a


def do_dance_move(dance_move, dancers):
    move_kind = dance_move[0]
    move = dance_move[1:]
    if move_kind == 's':
        spinners = int(move)
        spin(spinners, dancers)
    elif move_kind == 'x':
        move = move.split("/")
        exchange(int(move[0]), int(move[1]), dancers)
    elif dance_move[0] == 'p':
        move = move.split("/")
        partner(move[0], move[1], dancers)


for this_move in dance_moves:
    do_dance_move(this_move, dancing_programs)

dance_order = ""

for this_letter in dancing_programs:
    dance_order += this_letter

print("Part 1: " + dance_order)

final_counter = 0

for i in range(1, 1000000000):
    for this_move in dance_moves:
        do_dance_move(this_move, dancing_programs)
    if dancing_programs == start_positions:
        # Eventually it's going to cycle back to the beginning so we'll find
        # when that is so we don't have to do all 1 billion moves :)
        final_counter = 1000000000 % (i + 1)
        break


for i in range(0, final_counter):
    for this_move in dance_moves:
        do_dance_move(this_move, dancing_programs)

dance_order = ""
for this_letter in dancing_programs:
    dance_order += this_letter

print("Part 2: " + dance_order)
