def solution(nums):
    if nums is None or nums == []: return []

    nums.sort()
    return nums

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b
    
def break_chocolate(n, m):
    if n <= 0 or m <= 0: return 0
    return n*m-1

def is_anagram(test, original):
    def count_chars(s):
        res = {}
        # {"a": 1}
        
        for i in s:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
        
        return res
    
    return count_chars(test.lower()) == count_chars(original.lower())

def is_anagram(test, original):
    def count_chars(s):
        res = {}
        # {"a": 1}
        
        for i in s:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
        
        return res
    
    return count_chars(test.lower()) == count_chars(original.lower())

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number + 1,step))








def nb_dig(n, d):
    count = 0
    target = str(d)
    for i in range(n + 1):
        square_str = str(i * i)
        count += square_str.count(target)
    return count

def nb_dig(n, d):
    res = 0
    
    for i in range(n+1):
        sq = i**2
        
        res += str(sq).count(str(d))
        
    return res

def remove_url_anchor(url):
    if "#" in url:
        return url[:url.index("#")]
    else: return url

def capitals(word):
    res = []
    
    for i in range(len(word)):
        char = word[i]
        
        if char.isupper(): res.append(i)
    
    return res

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    
    result = 1
    for i in range(2, n+1):
        result *= i
    
    return result

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
