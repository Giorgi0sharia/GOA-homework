#pirveli davaleba
reverse_and_capitalize = lambda s: s[::-1].capitalize()

print(reverse_and_capitalize("hello"))      
print(reverse_and_capitalize("GOA"))      
print(reverse_and_capitalize("mamnd"))     

#meore davaleba
print((lambda x: x * 2)(5))

#mesame davaleba
numbers = list(range(1, 11)) 

print(list(map(lambda x: x**2, numbers)))