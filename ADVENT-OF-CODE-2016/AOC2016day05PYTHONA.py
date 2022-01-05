import hashlib

hash_string = "ffykfhsq"
hash_num = 0
password = ''

while len(password) != 8:
  MD5 = hashlib.md5((hash_string+str(hash_num)).encode('utf-8')).hexdigest()
  if MD5.startswith('00000'):
    password += MD5[5]
  hash_num += 1
press="The password is " +  password
print(press)
