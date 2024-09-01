import time
inputt=input("Enter your name\n")
timestamp = int(time.strftime('%H'))
print(timestamp)
if(timestamp>=12 & 18>=timestamp):
    print("Good Afternoon",inputt)

elif(timestamp>18 & 22<=timestamp):
    print("Good evining",inputt)
else:
    print("Good morning",inputt)


# https://docs.python.org/3/library/time.html#time.strftime