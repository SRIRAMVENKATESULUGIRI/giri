import re
pat=re.compile('([a-z]{4}[0-9]{2})@(google)(.com)')
mat=re.match(pat,"giri21@google.com")
if mat:
    print('pattern matched')
    print(mat.group(2))
else:
    print("pattern does not matched")