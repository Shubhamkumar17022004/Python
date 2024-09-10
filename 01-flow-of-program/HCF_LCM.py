# num1=int(input("Enter the number\n"))
# num2=int(input("Enter the number2\n"))

# smaller= num1 if num1<num2 else num2

# # FOR HIGHEST COMMON FACTOR
# temp=0
# for k in range(1,smaller+1):
#     if(num1 % k == 0 and num2 % k == 0):
#      temp=k
# print(temp)


# FOR LCM

num1=int(input("Enter the number\n"))
num2=int(input("Enter the number2\n"))

bigger= num1 if num1>num2 else num2

lcm=bigger

while(True):
    if(lcm%num1==0 and lcm%num2==0):
        break
    lcm = lcm+1
print(lcm)    