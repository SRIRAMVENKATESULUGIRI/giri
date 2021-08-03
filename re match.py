import re
pat=re.compile('[6|7|8|9]{1}[0-9]{9}')
mat=re.match(pat,'7896556445')
if mat:
    print("valid mobile number")
else :
    print ("invalid mobile number")