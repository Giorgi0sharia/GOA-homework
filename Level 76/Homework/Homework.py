def find_next_square(sq):
    
    # შევამოწმოთ თუ არის perfect square
    if int(sq**0.5)*int(sq**0.5) != sq: return -1

    # დავაბრუნოთ შემდეგი perfect square
    return (int(sq**0.5)+1)**2

def find_next_square(sq):
    if int(sq**0.5)*int(sq**0.5) != sq: return -1

    sq += 1
    while int(sq**0.5)*int(sq**0.5) != sq:
        sq += 1
    return sq

def longest(a1, a2):
    res = ""
    for i in a1:
        if i not in res: res += i
    for x in a2:
        if x not in res: res += x
    return "".join(sorted(res))

def longest(a1, a2):
    return "".join(sorted(set(a1+a2)))

def open_or_senior(data):
    res = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    
    return res


def row_sum_odd_numbers(n):
    start_num = 1
    res = []
    
    for i in range(1, n+1):
        ls = []
        for x in range(i):
            ls.append(start_num)
            start_num += 2
        res.append(sum(ls))
    
    return res[-1]


              