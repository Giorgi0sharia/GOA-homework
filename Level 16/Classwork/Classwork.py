

correct_password = 12345678
user_password = int(input("Input your password: "))
Password_Counter = 0

while correct_password != user_password:
    user_password = int(input("Input your password: "))
    Password_Counter += 1

print("you failed entering your password:" , Password_Counter, "times")


Correct_number = 6
print("Guess the correct single digit number!")
user_input_number = int(input("guess a number:"))
Counter = 0

while user_input_number != Correct_number:
    print("your number is incorrect, try again.")
    user_input_number = int(input("guess a number:"))
    Counter += 1

print("you Guessed correctly!", "you had" , Counter , "attempts")
