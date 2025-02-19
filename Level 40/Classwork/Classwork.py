#counting sheep
def count_sheeps(sheep):
    return sheep.count(True)

#remove empty spaces
def no_space(x):
    return x.replace(" ", "")

#double int
def double_int(i):
    return i*2

#return strings
def greet(name):
    return f"Hello, {name} how are you doing today?"

#convert bulleon to string
def boolean_to_string(b):
    return str(b)

#basic operator 
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    
#litres
def litres(time):
    return time // 2

#YEAR TO CENTURY

def century(year): 
    return (year + 99) // 100

#digitilize
def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list

#flower even or odd
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2)%2 == 1