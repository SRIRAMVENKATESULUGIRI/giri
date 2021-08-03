import re
pat=re.compile('[a-z]{6}[0-9]{4}@(gmail|yahoo).com')
mat=re.match(pat,'svgiri9441@yahoo.com')
if mat:
    print('pattern matched')
    print(mat)
else:
    print('pattern does not match')