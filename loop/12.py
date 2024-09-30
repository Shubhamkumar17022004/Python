# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print("")
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print("")
def print_rhombus_pattern(n):
    # Print the upper part of the rhombus
    for i in range(n):
        print(" " * i + "* " * (n - i))

    # Print the lower part of the rhombus
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

# Set the value of n
n = 5
print_rhombus_pattern(n)
