#pirveli davaleba
try:
    user_input = input("Please enter number: ")
    number = float(user_input)
    print(f"You entered the number {number}")
except ValueError:
    print(" That's not a number")

#meore davaleba
my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter an index access in the list"))
    print(f"Element at index {index} {my_list[index]}")
except IndexError:
    print("Index out of range")

#mesame davaleba
try:
    text = "GOA"
    number = 10
    result = text + number 
except TypeError:
    print(" Cannot add a string and an integer")