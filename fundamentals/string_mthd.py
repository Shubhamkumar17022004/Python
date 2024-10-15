str='apple is good'
print(str.replace("p",'s'))  #REPLACE METHOD

print(str.split(" ")) #split method
text = "Hello, world!"
words = text.split()
print(words)  # Output: ['Hello,', 'world!']

email = "user@example.com"
parts = email.split('@')
print(parts)  # Output: ['user', 'example.com']

# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 2, will return a list with 3 elements!
x = txt.split("#", 2)
print(x)

# ceter method in python
str1='welcome'
print(str1.center(18,"_"))


