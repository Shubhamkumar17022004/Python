# no=int(input("Enter first number\n"))
# no1=int(input("Enter the second no\n"))
# store=int(input("Enter 1 for addition , 2 for sub and 3 for mult"))
# match(store):
#  case _ if(store==1):
#   print("sum of two \"no\"",no,"+",no1,"=",no+no1)
#  case _ if(store==2):
#   print("sub of two no",no-no1)
#  case _:
#   print("Nothing foud")


week=int(input("Enter the no of week day"))
match(week):
 case 1:
  print("Monday")
 case 2:
  print("Tuesday")
 case 3:
  print("Wedensday")
 case 4:
  print("Thursday")
 case 5:
  print("Friday")
 case 6:
  print("Saturday")
 case 7:
  print("sunday")
 case _ :
  print("no data found on given particular number")

