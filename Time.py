import time
timestamp1 = time.strftime('17:05:05')
print(timestamp1)
hours = time.strftime('%H')
print(hours)

if(timestamp1 > hours ):
    print('Good Night')
elif(timestamp1 < hours):
    print('Good Evening')
else:
    print('Good Morning')
