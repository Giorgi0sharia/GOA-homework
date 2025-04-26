# 2) Lambda function to add 5 to a given number
add_five = lambda x: x + 5

# 3) Lambda function to multiply two numbers
multiply = lambda x, y: x * y

# 4) Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

# 5) Lambda function to convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

# 6) Lambda function to check if a string starts with 'A'
starts_with_A = lambda s: s.startswith('A')

# 7) Use map() to add 10 to every number in a list
numbers = [1, 2, 3, 4, 5]
add_ten = list(map(lambda x: x + 10, numbers))

# 8) Use map() to convert a list of strings to uppercase
words = ['hello', 'world', 'python']
uppercase_words = list(map(lambda s: s.upper(), words))

# 9) Use map() to find the length of each word in a list of strings
word_lengths = list(map(lambda s: len(s), words))

# 10) Use map() to square each number in a list
squares = list(map(lambda x: x**2, numbers))

# 11) Use map() to convert a list of integers to strings
string_numbers = list(map(lambda x: str(x), numbers))

# 12) Use map() to concatenate "Hello " to each name in a list
names = ['Alice', 'Bob', 'Charlie']
greetings = list(map(lambda name: "Hello " + name, names))

# 13) Use map() to subtract 5 from every element in a list
subtract_five = list(map(lambda x: x - 5, numbers))

# 14) Use map() to multiply each number in a list by 3
multiply_by_three = list(map(lambda x: x * 3, numbers))

# 15) Use map() to convert a list of temperatures from Celsius to Fahrenheit
temperatures_celsius = [0, 20, 37, 100]
temperatures_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_celsius))

# 16) Use map() to check if numbers in a list are greater than 50
check_greater_than_50 = list(map(lambda x: x > 50, numbers))

# 17) Use filter() to keep only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 18) Use filter() to select numbers greater than 10 from a list
nums = [5, 12, 19, 7, 3, 25]
greater_than_ten = list(filter(lambda x: x > 10, nums))

# 19) Use filter() to keep strings longer than 5 characters from a list of strings
words = ["apple", "banana", "cherry", "kiwi", "strawberry"]
long_words = list(filter(lambda w: len(w) > 5, words))

# 20) Use filter() to remove empty strings from a list of strings
strings = ["hello", "", "world", "", "python"]
non_empty_strings = list(filter(lambda s: s != "", strings))

# 21) Use filter() to select only positive numbers from a list
mixed_numbers = [-5, 3, 0, -2, 7, 10, -1]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))

# 22) Use filter() to keep names that start with the letter 'A' from a list of names
names = ["Alice", "Bob", "Andrew", "Charlie", "Anna"]
names_start_with_A = list(filter(lambda name: name.startswith('A'), names))

# 23) Use filter() to get numbers divisible by 3 from a list
numbers = [3, 5, 9, 12, 14, 18]
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))

# 24) Use filter() to keep words that contain the letter 'e' from a list of words
words = ["cat", "elephant", "dog", "eagle", "fish"]
words_with_e = list(filter(lambda w: 'e' in w, words))

# 25) Use filter() to remove all None values from a list
values = [1, None, 2, None, 3, 4, None]
non_none_values = list(filter(lambda x: x is not None, values))

# 26) Use filter() to keep numbers that are less than or equal to 50 from a list
numbers = [10, 55, 23, 78, 50, 99, 42]
less_than_equal_50 = list(filter(lambda x: x <= 50, numbers))
