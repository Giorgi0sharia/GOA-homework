#pirveli davaleba

num1 = int(input("enter ur number: "))
num2 = int(input("enter a second number: "))

if num1 > num2:
    print(num1)
else:
    print(num2)

#meore davaleba

num3 = int(input("Enter a number to find out if its odd even: "))

if num3 %2 ==0:
    print(num3 , "is even")
else:
    print(num3 , "is odd")

#mesame davaleba

num = int(input("Enter a number: "))

if num > 0:
    print(num , "positive")
elif num < 0:
    print(num , "is negative")
else:
    print("The number is zero")

#meotxe davaleba

num4 = int(input("Enter a number: "))

if num4 % 5 == 0:
    print(num4 ,"divisible by 5.")
else:
    print(num4 ,"not divisible by 5.")

#mexuti davaleba


for i in range(5):
    num = int(input(f"Enter number: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

#meeqvse davaleba

count = 0
password = input("Enter the password: ")

while password != "Goa best":
  count += 1
  print("Incorrect password, Try again.")
  password = input("Enter the password: ")

print("Correct password! You entered your password incorrectly", count, "times.")