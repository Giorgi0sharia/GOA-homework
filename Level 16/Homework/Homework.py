#pirveli davaleba
Times = 50
Counter = 0

while Times > 0:
    print("GOA IS THE BEST!")
    Times -= 1
    Counter += 1
print("GOA IS THE BEST! was printed" , Counter , "times")

Counter2 = 0
for i in range(50):
    print("GOA IS THE BEST")
    Counter2 += 1
print("GOA IS THE BEST! was printed" , Counter2 , "times")

#meore davaleba
num1 = 0

while num1 < 11:
    print(num1)
    num1 += 1

#mesame davaleba

num2 = 1

while num2 < 21:
        if num2 % 2 == 0:
            print(num2)
            num2 += 1 

#meotxe davaleba

num1 = 10

while num1 > 0:
    print(num1)
    num1 -= 1
print("blastoff")

#mexute dabavaleba

correct_password = 213901
user_promted_password = int(input("Input your password: "))
Password_Counter = 0

while correct_password != user_password:
    user_password = int(input("Input your password: "))
    Password_Counter += 1

print("you put the wrong passowrd:" , Password_Counter, "times")

#meeqvse davaleba

correct_username = "Abefall"
correct_password = 213901

user_promted_username = input("Input your username: ")
user_promted_password = int(input("Input your password: "))
Username_Counter = 0
Password_Counter = 0

while correct_username != user_promted_password:
    user_promted_username = int(input("Input your username: "))
    Username_Counter += 1

while correct_password != user_promted_password:
    user_password = int(input("Input your password: "))
    Password_Counter += 1

print("you put your wrong Username:" , Username_Counter, "times and")
print("you put your wrong passowrd:" , Password_Counter, "times")

#meshvide davaleba

number = int(input("input a number:"))
factorial = 1

while number > 1:
    factorial *= number
    number -= 1
print("The factorial of the number you have selected is:", factorial)