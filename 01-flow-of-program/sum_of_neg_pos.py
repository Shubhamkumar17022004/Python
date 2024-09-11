# Write a program to print the sum of negative numbers, sum of positive even numbers and the sum of 
# positive odd numbers from a list of numbers (N)entered by the user. The list terminates when the 
# user enters a zero.

print("FOR EXIT PLZ ENTER 0")
sumn=0
sump=0
sumod=0
while(True):
    num=int(input("Enter the number"))
    if(num==0):
       break
    elif(num<0):
        sumn=sumn+num
    elif(num>0 and num%2==0):
        sump=sump+num
    else:
        if(num%2!=0):
         sumod=sumod+num
print("Sum of -ve number is",sumn)
print("Sum of +ve even number is",sump)
print("Sum of odd number is",sumod)
