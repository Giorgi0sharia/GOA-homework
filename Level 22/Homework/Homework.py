#davaleba pirveli
list1=[1,54,9.8,75,True,4,"apple",9,10,False]

print(list1[0:10:1])

#davaleba meore

num1,num2=int(input("INPUT A NUMBER: ")),int(input("INPUT A NUMBER: "))

if num2 > num1:
    print(list1[num1:num2:1])
elif num1 > num2:
    print(list1[num2:num1:1])
elif num1 == num2:
    print(list1[num1:num2])

#davaleba mesame
print("first", list1[0],"third",list1[2],"last",list1[9])

#davaleba meotxe
list2 = ["apple","banana","citrus","watermellon","grape"]
print(list2[-1:-6:-1])

#davaleba meeqvse
print(list2[0:5:2])

#davaleba mecxre
list3=[1,54,9.8,75,4,9,10]
list3[3]=100

print(list3)