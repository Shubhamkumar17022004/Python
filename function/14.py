def hcf(n1,n2):
    temp=1
    minm= n1 if n1<n2 else n2
    for i in range(1,minm+1):
        if(n1%i==0 and n2%i==0):
            temp=i
    return temp
print(hcf(1,7))
