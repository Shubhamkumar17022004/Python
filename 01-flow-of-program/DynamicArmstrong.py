import math
no=int(input("Enter the number\n"))
no1=no
count=0
while(no!=0):
    num=no%10
    count=count+1
    no=no//10

sum=0
temp=no1
while(no1!=0):
    rem=no1%10
    sum=int(sum+math.pow(rem,count))
    no1=no1//10
if(temp==sum):
    print("Armstrong")
elif(temp!=sum):
    print("not Arm")
else:
    print("Enter valid input")
