no1=int(input("pleaser Enter the first number\n"))
no2=int(input("please Enter the second number\n"))
no3=int(input("please Enter the 3rd no\n"))

#THIS IS AN EXAMPLE OF IF

# if(no1>no2):
#     print(no1,"is greater")
# else:
#     print(no2,"is greater")

#THIS IS AN EXAMPLE OF ELIF

# if(no1>=no2 and no1>=no3):
#     print(no1,"is greater a")

# elif(no2>=no1 and no2>=no3):              
#     print(no2,"is greater")

# elif(no3>=no1 and no3>=no2):
#     print(no3,"is greater")
# else:
#     print("please enter the valid number only")


#THIS IS AN EXAMPLE OF NEXTED IFELIF

if(no1>no2):
    if(no1>no3):
     print("no1 is grater")
    else:
     print("c is greater")
elif(no2>no1):
  if(no2>no3):
    print("no2 is greater")
  else:
    print("no3 is greater")
else:
  print("Enter the valid data")

