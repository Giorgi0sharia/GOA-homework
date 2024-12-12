#pirveli davaleba
num1, num2, num3 = int(input("please input a number: ")) , int(input("please input a number: ")) , int(input("please input a number: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 >num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)

#meore davaleba
grade = int(input("Please input your grade: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
elif grade < 60:
    print("F")

#mesame davaleba

num4 = int(input("Please input a number: "))

if num4 > 0:
    print("The number youve inputted is positive.")
elif num4 < 0:
    print("The number youve inputted is negative.")
elif num4 == 0:
    print("The number youve inputted is zero.")

#meotxe davaleba

num5 = int(input("Please input a number: "))
num6 = int(input("Please input a number: "))

sum = 0

for i in range(num5, num6 + 1):
    sum += i

print("The sum of the numbers between", num5 ,"and", num6,"is", sum)

#mexute davaleba

num6 = int(input("Please input a number: "))

if num6 <= 1:
    print(num6, "is not a prime number.")
else:
    for i in range(2, num6):
        if num6 % i == 0:
            print(num6, "is not a prime number.")
            break
    else:
        print(num6 , "is a prime number.")

#meeqvse davaleba

numbers = [10, 25 ,120 ,687 , 17]

print("First number", numbers[0])
print("Third number", numbers[2])
print("Fifth number", numbers[4])

#meshvide davaleba

list = [2 , "Banana" , 6.97 , False , 42 , "Tree" , 102, 3.1415 , "car", False, 77, 93, "green", [1,5,"red"], 5, True, 0.6 , 16, False, "black"]

for i in range(len(list)):
    print("The element on", i, "is", list[i])

