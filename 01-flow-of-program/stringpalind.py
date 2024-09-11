user=input("Enter the string tho check for palindrome\n")
# store=' '.join(user.strip().lower())
store = ''.join(user.split()).lower()  # 'amanaplanacanalpanama'

reverse=store[::-1]
if(store==reverse):
    print("Palindrome")
else:
    print("Not palindrome")


# user=input("Enter the string tho check for palindrome\n")

# length=len(user)
# mid=length//2

# first=user[:mid]
# print(first)

# second=user[mid+1:]
# print(second)

# if(first == second[::-1]):
#     print("Palindrome")
# else:
#     print("not palindrome")
