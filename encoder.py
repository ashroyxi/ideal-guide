import string
import random

given = input("Enter message to encrypt:\t")

#algorithm
before = string.ascii_lowercase + string.ascii_uppercase
after = string.ascii_lowercase.replace("ab", "") + "ab" + string.ascii_uppercase.replace("AB", "") + "AB"
dictionary  = str.maketrans(before, after)

enc_nosalt = given.translate(dictionary)

#adding salt
x = enc_nosalt.split()
super_list = [list(a) for a in x]
salted = []
for i in super_list:
    part = [x + random.choice(string.ascii_letters) for x in i]
    salted = salted + part + [" "]

#post Processing
salted.pop()
encoded = ''.join(salted)
print(encoded)
input("Do anything to exit")
