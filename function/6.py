def prime(n):
    if n<2:
        print("please enter greater then 2")
        return
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count==2):
        print("It's prime number")
    else:
        print("It's not prime")
prime(1)