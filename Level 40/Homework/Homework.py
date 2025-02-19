#pirveli davaleba (axsna)

#counting sheep
def count_sheeps(sheep):
    return sheep.count(True)
#AQ viyenebt count funqcias


#remove empty spaces
def no_space(x):
    return x.replace(" ", "")
#aq replace funqcii spaces vcvlit sicarieleshi

#double int
def double_int(i):
    return i*2
#aq vaormagebt


#return strings
def greet(name):
    return f"Hello, {name} how are you doing today?"
#aq viyenebt f funqcias

#convert bulleon to string
def boolean_to_string(b):
    return str(b)
#aq viyenebt str funqcias romlis sashualebitac vcvlit booleans stringad

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
#aq vqmnit martiv calculator

#litres
def litres(time):
    return time // 2

#YEAR TO CENTURY
def century(year): 
    return (year + 99) // 100

#digitilize
def digitize(n):
    #vqmnit starting strs
    starting_str = str(n)

    #vadefinebt reversed strs
    reversed_str = starting_str[::-1]

    #es iqneba chveni saboloo sia
    res_list = []

    #aq titoeul reversed_str components appendis sashualebit vdebt res_listshi
    for i in reversed_str:
        res_list.append(int(i))

    return res_list

#flower even or odd
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2)%2 == 1
#luwi da kentis jami yoveltvis luwia, amit varkvevt mocemuli piroba true tu falsia


#meore davaleba (vwert amocanebs)

#Beginner Series #1 School Paperwork

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

#MakeUpperCase
def make_upper_case(s): 
    return s.upper()

#Beginner Series #2 Clock
def past(h, m, s):
    if h < 0 or m < 0 or s < 0:
        return 0
    return (h * 3600 + m * 60 + s) * 1000

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
#Abbreviate a Two Word Name
def abbrev_name(name):
    first_name, last_name = name.split()

    return f"{first_name[0].upper()}.{last_name[0].upper()}"