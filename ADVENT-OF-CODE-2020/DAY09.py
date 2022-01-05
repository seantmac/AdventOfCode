value_list = [int(el) for el in open('9.TXT', 'r').read().splitlines()]


## Part 1:
def has_sum(int_list, value):
    is_sum = False
    i = 0

    while not is_sum and i < len(int_list):
        is_sum = (value - int_list[i]) in int_list
        i += 1

    return is_sum


def get_numb_not_sum(input_list, preamb):
    preamble = preamb
    int_list = input_list.copy()

    i = preamble
    while has_sum(int_list[i - preamble:i], int_list[i]):
        i += 1
    else:
        return int_list[i]


invalid_number = get_numb_not_sum(value_list, 25)
print("Part 1  ", invalid_number)

##  Part  2:
def get_encrypt_weakness(input_list, inval_n):
    inval_numb = inval_n
    int_list = input_list.copy()

    for i in range(0, int_list.index(inval_numb)):
        j = i + 2
        li_sum = sum(int_list[i:j])
        while li_sum < inval_numb:
            j += 1
            li_sum = sum(int_list[i:j])
        else:
            if li_sum == inval_numb:
                return min(int_list[i:j]) + max(int_list[i:j])


p2 = get_encrypt_weakness(value_list, invalid_number)
print("Part 2  ", p2)

## Part 1   70639851
## Part 2   8249240