def triplet(n1,n2,n3):
    sq1=n1*n1
    sq2=n2*n2
    sq3=n3*n3
    sum=sq1+sq2
    if sq1 + sq2 == sq3 or sq1 + sq3 == sq2 or sq2 + sq3 == sq1:
        print("Triplet")
    else:
        print("Not triplet")
triplet(3,5,4)