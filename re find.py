import re
pat=re.compile('black')
mat=re.findall(pat,'black truck on the black road')
if mat:
    print("pattern matched")
    print(mat)
else:
    print("pattern not mached")