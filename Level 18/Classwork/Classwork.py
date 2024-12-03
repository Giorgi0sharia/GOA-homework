#pirveli davaleba
for i in range(0, 20, 2):
    print(i)

#meore

for i in range(1, 20, 2):
    print(i)


#mesame
num = 1

for num in range(1, 31):
    if num % 2 == 0:
        print(num,"is even")
    else:
        print(num ,  "is odd")

#meotxe

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    for num in range(num2, num1 + 1):
        if num % 2 == 0:
            print(num, "is even")
else:
    for num in range(num1, num2 + 1):
        if num % 2 != 0:
            print(num, "is odd")

    