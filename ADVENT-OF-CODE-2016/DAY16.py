def next_str(s):
    b = ''.join('0' if c == '1' else '1' for c in reversed(s))
    return '{}0{}'.format(s, b)


def checksum(s):
    l = []
    for a, b in zip(s[::2], s[1::2]):
        if a == b:
            l.append('1')
        else:
            l.append('0')
    if len(l) % 2 != 0:
        return ''.join(l)
    else:
        return checksum(''.join(l))


def gen(start, l):
    while (len(start) < l):
        start = next_str(start)
    return start[:l]


#start = "10010000000110000"
start = "01111001100111011"
print(checksum(gen(start, 272)))
print(checksum(gen(start, 35651584)))


#11111000111110000
#10111100110110100