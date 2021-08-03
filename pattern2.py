import re
pat=re.compile('bat')
mat=re.findall(pat,'batdhonibat')
if mat:
    print('pattern matched')
    print(mat)
else:
    print('pattern does not match')


# match()-match only at the beginning
# search()-search anywhere in the string
# findall()-find all match in the string
