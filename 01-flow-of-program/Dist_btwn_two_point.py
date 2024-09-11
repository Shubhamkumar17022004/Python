import math
x1=int(input("Enter the value of x1\n"))
x2=int(input("Enter the value of x2\n"))
y1=int(input("Enter the value of y1\n"))
y2=int(input("Enter the value of y2\n"))

distx=x2-x1
print(distx)
disty=y2-y1

dist= math.sqrt((distx*distx)+(disty*disty))

print(dist)