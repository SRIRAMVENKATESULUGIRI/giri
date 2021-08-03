import re
pat=re.compile('https?')
mat=re.match(pat,'https://www.google.com')
if mat:
    print('valid URL')
    
else:
    print('invalid URL')
    