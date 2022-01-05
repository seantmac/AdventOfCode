password = "vzbxkghb"
alphabet = "abcdefghjkmnpqrstuvwxyz"

def increment_position(password,location):
    current_letter = password[location]
    new_letter = alphabet[(alphabet.index(current_letter)+1)%23]
    password = password[:location] + new_letter + password[location+1:]
    if new_letter == 'a':
        return increment_position(password,location-1)
    else:
        return password

def count_double_pairs(password):
    if len(password) < 2:
        return 0
    elif password[0] == password[1]:
        return 1 + count_double_pairs(password[2:])
    else:
        return count_double_pairs(password[1:])

def ordered(password):
    return any(ord(x1)+2 == ord(x2)+1 == ord(x3) for x1,x2,x3 in zip(password,password[1:],password[2:]))

def good_password(password):
    return ordered(password) and count_double_pairs(password) >= 2

def next_good_password(password):
    password = increment_position(password,len(password)-1)
    while not good_password(password):
        password = increment_position(password,len(password)-1)
    return password

password = next_good_password(password)
print(password)
password = next_good_password(password)
print(password)


#vzbxxyzz
#vzcaabcc

#wrongers:
#Next password: waaaaabc
#Next next password: waaaabca