import hashlib
import re

hash_string = "ffykfhsq"
hash_num = 0
password = '*'*8

while '*' in password:
  MD5 = hashlib.md5((hash_string+str(hash_num)).encode('utf-8')).hexdigest()
  if re.search('^00000[0-7]', MD5):
    if password[int(MD5[5])] == '*':
      password = password[:int(MD5[5])] + MD5[6] + password[int(MD5[5])+1:]
      print(password)
  hash_num += 1

press="The password is " +  password
print(press)
