rang=5
n1=0
n2=1
if(rang==0):
    exit()
if(rang==1):
    print(n1)
    exit()
print(n1)
print(n2)
for k in range(1,rang-1):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum)