def palindrome(no):
    sum=0
    while(no!=0):
        revr=no%10
        sum=sum*10+revr
        no=no//10
        print(sum)
palindrome(111)