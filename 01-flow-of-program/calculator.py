num=int(float(input("Enter the first num\n")))
num2=int(float(input("Enter the second num\n")))
operation=input(("Enter the + for addition and - for sub and * for mult and / for devide and % for modulo\n"))
match operation :
 case "+" :
  print("addition of two number is", num+num2)
 case "-" :
  print("subtraction of 2 number is",num-num2)
 case "/" :
  print("Divide of two number is", num/num2)
 case "%" :
  print("Modulo of 2 number is",num%num2)
 case "*" :
  print("Mult of 2 number is",num*num2)