# 2) Print your name
print("John Doe")

# 3) Print a favorite quote
print('"The only limit to our realization of tomorrow is our doubts of today."')

# 4) Print multiple lines
print("Roses are red,")
print("Violets are blue,")
print("Python is fun too!")

# 5) Print a simple math result
print(2 + 3)

# 6) Print a shape with symbols
print("  *  ")
print(" *** ")
print("*****")

# 7) Convert string to integer
num_str = "42"
num = int(num_str)
print(num)

# 8) Add two floats
a = 3.5
b = 2.5
print(a + b)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 10) Print data types
x = 10
y = "Python"
z = 3.14
print(type(x))
print(type(y))
print(type(z))

# 11) User input and type conversion
age = int(input("Enter your age: "))
print("Next year you will be:", age + 1)

# 12) Ask for your name
name = input("What is your name? ")
print("Hello, " + name + "!")

# 13) Ask for age and calculate next year’s age
age = int(input("How old are you? "))
print("Next year you will be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# 15) Favorite color
color = input("What is your favorite color? ")
print("Your favorite color is " + color + "!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough!")
else:
    print("You are not tall enough.")

# 17) Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
word = "Python"
for letter in word:
    print(letter)

# 19) Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum is:", total)

# 20) Multiplication table (1 to 5)
for i in range(1, 6):
    print(f"2 x {i} = {2*i}")

# 21) Even numbers 2 to 20
for i in range(2, 21, 2):
    print(i)

# 22) Print numbers from 1 to 5 using while
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5 using while
i = 1
sum_ = 0
while i <= 5:
    sum_ += i
    i += 1
print("Sum:", sum_)

# 24) Count down from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print odd numbers between 1 and 10
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 26) Ask until user enters "exit"
while True:
    text = input("Enter something (type 'exit' to quit): ")
    if text.lower() == "exit":
        break

# 27) Print all elements of a list
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# 28) Find the length of a list
my_list = [1, 2, 3, 4]
print(len(my_list))

# 29) Access a specific element
nums = [10, 20, 30]
print(nums[1])

# 30) Add element to list
my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list)

# 31) Remove an element
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list)

# 32) List of squares
squares = [x**2 for x in range(1, 6)]
print(squares)

# 33) List of even numbers
evens = [x for x in range(2, 11, 2)]
print(evens)

# 34) Filter odd numbers
nums = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in nums if x % 2 != 0]
print(odds)

# 35) Strings to uppercase
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
print(upper_words)

# 36) Squares if divisible by 2
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums if x % 2 == 0]
print(squares)

# 37) Function to greet a user
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 38) Function to add two numbers
def add(a, b):
    return a + b

print(add(5, 7))

# 39) Even or odd function
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_or_odd(4))

# 40) Area of a rectangle
def area(length, width):
    return length * width

print(area(5, 3))

# 41) Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# 42) Create and print a tuple
t = (1, "hello", 3.14)
print(t)

# 43) Access element in a tuple
print(t[1])

# 44) Length of a tuple
print(len(t))

# 45) Concatenate tuples
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# 46) Check if item in tuple
if 2 in t1:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
s = {1, 2, 3}
print(s)

# 48) Check if element in set
if 2 in s:
    print("Yes")
else:
    print("No")

# 49) Add element to set
s.add(4)
print(s)

# 50) Remove element from set
s.remove(2)
print(s)

# 51) Union of sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# 52) Create and print dictionary
d = {"name": "Alice", "age": 25}
print(d)

# 53) Access value by key
print(d["name"])

# 54) Add key-value to dictionary
d["city"] = "New York"
print(d)

# 55) Basic variable assignment
a = "code"
b = "wa.rs"
name = a + b

# 56) get character from ASCII Value
def get_char(c):
    return chr(c)