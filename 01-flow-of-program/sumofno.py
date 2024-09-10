print("IF YOU WANT EXIT THEN PRESS 0")
sum=0
while(True):
    number=int(input("Enter the number "))
    if(number==0):
        break
    sum=sum+number
print("sum of the numbers are"," ",sum)