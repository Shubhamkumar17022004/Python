for x in range(6):
    if x==5:
     break
    print(x)
else:
   print("finally end")  #IN THIS CODE THE ELSE WILL NOT PRINT ANYTHING BECAUSE AFTER THE break
                          #KEYWORD NOTHING WILL EXECUTE.SO WE NEED TO USE PRINT ONLY


for x in range(6):
    print(x)
else:
   print("finally end")  #IN THIS CODE THE ELSE WILL PRINT because dont use break


for x in range(6):
    if(x==6):
       break
    print(x)
else:
   print("finally end")  #IN THIS CODE THE ELSE WILL execute because the break 
                              #will not execute anytime


for i in range(4):
 if i==2:
  print(i)
 i=10
 print(i)   #see the output