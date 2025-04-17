#Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        cur_num = arr[i]
        prev_num = arr[i-1]
        
        if cur_num - prev_num > 1: return cur_num
    
    return None

#altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return string.swapcase()

#Correct the mistakes of the character recognition software
def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")

#is it a palidrome
def bonus_time(salary, bonus):
    if bonus == True:
        return f"${salary*10}"
    return f"${salary}"

#Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus == True:
        return f"${salary*10}"
    return f"${salary}"

#Student's Final Grade
def final_grade(exam, projects):
    if exam > 90 or projects > 10: return 100
    elif exam > 75 and projects >= 5: return 90
    elif exam > 50 and projects >= 2: return 75
    return 0

#Sum The Strings
def sum_str(a, b):
    if len(a) > 0 and len(b) == 0: return a
    elif len(a) == 0 and len(b) > 0: return b
    elif len(a) == 0 and len(b) == 0: return "0"

    return str(int(a) + int(b))

#expressions matter
def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)

#I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"

#Reverse List Order
def reverse_list(l):
    l.reverse()
    return l

#count odd numbers below n
def odd_count(n):
    return n//2

#diffrence in values of cuboids
def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    
    if v_a > v_b: return v_a - v_b
    return v_b - v_a

#Welcome!
def greet(language):
    all_lang = [ 
        ("english", "Welcome")
        , ("czech", "Vitejte")
        , ("danish", "Velkomst")
        , ("dutch", "Welkom")
        , ("estonian", "Tere tulemast")
        , ("finnish", "Tervetuloa")
        , ("flemish", "Welgekomen")
        , ("french", "Bienvenue")
        , ("german", "Willkommen")
        , ("irish", "Failte")
        , ("italian", "Benvenuto")
        , ("latvian", "Gaidits")
        , ("lithuanian", "Laukiamas")
        , ("polish", "Witamy")
        , ("spanish", "Bienvenido")
        , ("swedish", "Valkommen")
        , ("welsh", "Croeso")
    ]
    
    for key in all_lang:
        if key[0] == language: return key[1]
    
    return "Welcome"

#Drink about
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
#sort and star
def two_sort(array):
    array.sort()
    
    res = ""
    for i in array[0]:
        res += i+"***"
    
    return res[:-3]

#grasshopper - messi goals
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

#short story long
def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
    
#My head is at the wrong end!
def fix_the_meerkat(arr):
    arr.reverse()
    return arr

#find multiples of a number
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]

#unfinished loop - bug fixing
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1 
    return res
    
