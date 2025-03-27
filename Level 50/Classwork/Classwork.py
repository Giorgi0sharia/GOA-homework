#1 pirveli davaleba

number = 5

try:
    result = number + "string"
except TypeError as e:
    print(f"TypeError: {e}") 


# 2 meore davaleba
try:
    name = input("შეიყვანეთ თქვენი სახელი: ") 
    if len(name) == 0:
        raise ValueError("სახელი არ უნდა იყოს ცარიელი")
    print(f"თქვენი სახელი: {name}")
except ValueError as e:
    print(e) 
except Exception:
    print("გახდილია შეცდომა")