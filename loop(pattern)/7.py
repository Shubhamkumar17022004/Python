for i in range(1,5):
    for j in range(i,4):
        print(" ",end="")
    for k in range(i):
        print("*",end="")

    # for l in range(i):
    #     print(" ",end="")
    for m in range(i-1):
        print("*",end="")
    print("\n")
