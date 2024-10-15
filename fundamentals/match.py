match 10:
    case 0:
        print("hello 0")
    case 1:
        print("hello 1")
    case _:
        print("no data found")

value=int(input("Enter the integer value"))
match value:
    case 1:
        print("hello")
    case 2:
        print("shubham")
    case _:
        print("Nothing")

value1 = int(input("Enter the integer value: "))
match value1:
    case x if x > 0:
        print("+ve")
    case x if x < 0:
        print("-ve")
    case _:
        print("Nothing")

value1 = int(input("Enter the integer value: "))
match value1:
    case _ if value1 > 0:
        print("+ve")
    case _ if value1 < 0:
        print("-ve")
    case 0:
        print("Nothing")
