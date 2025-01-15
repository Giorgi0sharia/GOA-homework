#pirveli davaleba

name = input("შეიყვანეთ თქვენი სახელი: ")


choice = input("შეიყვანეთ არჩევანი (u ან l): ")

if choice == 'u':
    print(name.upper())  
elif choice == 'l':
    print(name.lower())  
else:
    print("wrong information")  

#meore davaleba

def manual_find(main_string, str_to_find):
    index = main_string.find(str_to_find)
    print(index)

main_string = input("შეიყვანეთ მთავარი: ")
str_to_find = input("შეიყვანეთ საძიებელი: ")

manual_find(main_string, str_to_find)

#mesame davaleba

main_str = input("შეიყვანეთ მთავარი სთრინგი: ")

str_to_count = input("შეიყვანეთ რისი დათვლაც გინდათ: ")


count = main_str.count(str_to_count)
print(count)
    
#meotxe davaleba

def manual_swapcase(input_str):
    result = ""
    for i in input_str:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    print(result) 

text = "Hello World!"
new_text = manual_swapcase(text)
print(new_text)
