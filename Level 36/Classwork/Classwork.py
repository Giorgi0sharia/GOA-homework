def multiply(a, b):
    return a * b

#Even or Odd
def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else: return "Odd"

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversed Strings
def solution(string):
    return string[::-1]

#Return Negative
def make_negative( number ):
    if number > 0:
        return number * -1
    else: return number

#Opposite number
def opposite(number):
    return number * -1

#convert buleon yes to no
def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    else:
        return "No"
#sum
def positive_sum(arr):
    res = 0
    for i in arr:
        if i > 0:
            res += i
    return res
#repeat
def repeat_str(repeat, string):
    res = ""
    for i in range(repeat):
        res = res + string
    return res

#remove first and last
def remove_char(s):
    return s[1:-1]

def square_sum(numbers):
    result=0
    for i in numbers:
        result+=i**2
    return result