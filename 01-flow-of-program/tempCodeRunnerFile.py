user=input("Enter the string tho check for palindrome")
reverse=user[::-1]
if(user==reverse):
    print("Palindrome")
else:
    print("Not palindrome"