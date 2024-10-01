def maxm(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print("N1 is greater",n1)
    elif(n2>n3 and n2>n1):
        print("N2 is greater",n2)
    else:
        print("N3 is greater",n3)
 
def minm(n1,n2,n3):
    if(n1<n2 and n1<n3):
        print("N1 is Smaller",n1)
    elif(n2<n3 and n2<n1):
        print("N2 is Smaller",n2)
    else:
        print("N3 is Smaller",n3)

maxm(2,4,10)
minm(2,-4,7)