# The in operator is used to check if a specific element 
# is present within a sequence (like a list, tuple, string, or dictionary).
# It returns a Boolean value: True if the element is found, False otherwise.


# The is operator in Python is used to check if two objects are the same object in memory. 
# It's different from the == operator, which compares the values of objects.

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is present.")
else:
    print("Banana is not present.")

text = "Hello, world!"
if "world" in text:
    print("The word 'world' is in the text.")
else:
    print("The word 'world' is not in the text.")


person = {"name": "Alice", "age": 30}
if "age" in person:
    print("The key 'age' is in the dictionary.")
else:
    print("The key 'age' is not in the dictionary.")

person = {1,2,3,4,5}
if 3 in person:
    print("The key is in the dictionary.")
else:
    print("The key is not in the dictionary.")

#is operator

x = 5
y = 5

if x is y:
    print("x and y are the same object.")
else:
    print("x and y are different objects.")