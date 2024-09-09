input=int(input("Enter the year to check for leap year\n"))
if((input % 4 == 0 and input % 100 !=0 ) or (input % 400 == 0)):
    print("Leap year")
else:
    print("Not a leap year")