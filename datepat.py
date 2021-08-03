import re
pat=re.compile('(\\d\\d)-(\\d\\d)-(\\d\\d\\d\\d)')
mat=re.match(pat,'21-04-2021')
if mat:
    print('pattern matched')
    print(mat.group(0))
    print(mat.group(1))
    print(mat.group(2))
    print(mat.group(3))
else:
    print('pattern does not match')
 # \\d-[0-9]