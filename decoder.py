import string

#remove salt
encoded = input("Enter the encoded string: \t").split()
super_list = [list(x) for x in encoded]
unsalt = []
for i in super_list:
    unsalt = unsalt + i[0::2] + [" "]


unsalted = ''.join(unsalt)
#translate
after = string.ascii_lowercase + string.ascii_uppercase
before = string.ascii_lowercase.replace("ab", "") + "ab" + string.ascii_uppercase.replace("AB", "") + "AB"
dictionary  = str.maketrans(before, after)

decoded = unsalted.translate(dictionary)
print("Decoded string:" , decoded)
input("Do anything to exit")
