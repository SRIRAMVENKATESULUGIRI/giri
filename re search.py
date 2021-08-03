import re
pat=re.compile("@gmail.com")
mat=re.search(pat,'svgiri9441@gmail.com')
if mat:
    print("valid gmail id")
else:
    print("invalid gmail id")