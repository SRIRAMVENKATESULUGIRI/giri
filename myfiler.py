f=open('D:\\giri.txt','w+')
f.write('cryptocurrency is ruling the world')
print(f.tell())  # position of file pointer(cursor)
f.seek(0,0)  # go to file beginning
print(f.read())
f.close()