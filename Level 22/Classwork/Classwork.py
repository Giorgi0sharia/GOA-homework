list1 = [1,5,6,11,"Apple",True,20,17,0.67,10]

num1 = int(input("Input a number:"))

if num1 <= 8 or num1 >= 0:
    print(list1[num1])
elif num1 >= -10 or num1 <= -1:
    print(list1[num1])


list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list2:
    print(x*2)
    print(x/2)