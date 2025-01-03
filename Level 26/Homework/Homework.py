#pirveli davaleba

def sum(num1,num2):
    print(num1+num2)

sum(5,6)
sum(int(input("input a number:")) , int(input("input a number:")) )

#daveleba ori

def even_or_odd(number):
    if number % 2 == 0:
        print(number , "is even")
    else:
        print(number , "is odd")

even_or_odd(7)
even_or_odd(int(input("input a number:")))


#mesame davaleba

def reverse_string(string):
    reversed_string = string[::-1]
    print(reversed_string)

reverse_string("Hello")
reverse_string(input("input a text to be reversed:"))

#meotxe davaleba

numbers = [5, 2, 9, 1, 7]

def find_max(numbers):
    print(max(numbers))

find_max([5, 2, 9, 1, 7])

#mexute davaleba

def factorial(n):
  if n < 0:
     print("Your number is a negative")
  else:
    fact = 1
    for i in range(1, n + 1):
      fact *= i
    print(fact)

factorial(7)


