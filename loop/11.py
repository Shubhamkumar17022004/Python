for i in range(5,0,-1):
    for j in range(5-i):
        print("_",end="")
    for k in range(i):
        print("*",end=" ")
    print("")
