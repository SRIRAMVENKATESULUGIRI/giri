import datetime
today=datetime.datetime.now()
print(today)
myday=today.strftime('%d-%m-%Y')
print(myday)
s='11-09-10 12:15:10'
newdate=today.strptime(s,'%d-%m-%y %H:%M:%S')
print(newdate)
mytime=today.strftime("%H:%M:%S")
print(mytime)