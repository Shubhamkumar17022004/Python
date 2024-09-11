no=28
sum=0
for k in range(1,no):
    if(no%k==0):
        print("Divisor of {no} are",k)
        sum=sum+k
if(sum==no):
     print("perfect No")
else:
       print("not perfect")
    