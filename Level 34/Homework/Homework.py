#pirveli davaleba

print("Hello World!")

#meore davaleba
def calculate_the_sum(num1,num2):
    print(num1 + num2)

num1 = int(input("Please input your num1: "))
num2 = int(input("Please input your num2: "))
calculate_the_sum(num1,num2)

#mesame davaleba
def times_by_10(num3):
    print(num3 * 10)

num3 = int(input("Please input your num3: "))

times_by_10(num3)

#meotxe davaleba
def greeting(username="Guest"):
    print(f"Hello, {username}")

greeting()
greeting("george")

#mexute davaleba
def outer_function():
    def inner_function():
        print("This is the inner function.")
    
    inner_function()

outer_function()

#meeqvse davaleba

def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

magaliti = [1, 2, 3, 4, 5, 6]
check_even_odd(magaliti)

#meshvide davaleba

def find_highest(list_of_number):

    maxnum = list_of_number[1]

    for i in list_of_number:
        if i > maxnum:
            maxnum = i
    print(f"The maximum number is: {maxnum}")

numbers_list = [3, 5, 7, 2, 8, 1]
find_highest(numbers_list)

#merve davalevba

def make_positives_list(number2):
    positive_numbers = []
    for i in number2:
        if i > 0:
            positive_numbers.append(i)
    print(positive_numbers)


numbers_list2 = [-3, 5, -1, 7, 0, -4, 9]
positive_numbers = make_positives_list(numbers_list2)

#mecxre davaleba
def sum_divisible_by_3(start, end):
    total_sum = 0  
    
    for num in range(start, end + 1):  
        if num % 3 == 0:
            total_sum += num
    print(f"The total sum of numbers divisible by 3 is: {total_sum}")

sum_divisible_by_3(1, 100)