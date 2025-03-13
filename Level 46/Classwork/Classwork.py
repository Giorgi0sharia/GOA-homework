#საკლასო დავალება:

#შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

#თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

#ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def manual_list(start, end, step, user_num):
    return [num + user_num for num in range(start, end, step)]

print(manual_list(1, 10, 2, 3))
print(manual_list(5, 20, 4, 5))
print(manual_list(0, 15, 3, 2)) 

#Create a list comprehension that generates a list of all numbers between 1 and 100 that are divisible by either 3 or 5, but not both.
numbers = [i for i in range(1, 101) if (i % 3 == 0) != (i % 5 == 0)]
print(numbers)

#Create a list comprehension that generates a list of all palindromic numbers between 10 and 200 (a palindromic number reads the same forward and backward).
palindromic_numbers = [num for num in range(10, 201) if str(num) == str(num)[::-1]]
print(palindromic_numbers)