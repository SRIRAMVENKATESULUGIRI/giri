import re
pat=re.compile('([a-z]+)@([a-z]+)(.com)')
mat=re.match(pat,'giri@microsoft.com')
if mat:
    print('empname:',mat.group(0))
    print('empname:',mat.group(1))
    print('companyname:',mat.group(2))
    
    
else:
    print('invalid mobile number')