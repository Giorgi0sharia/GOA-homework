#Disemvowel Trolls
def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res

#Square Every Digit
def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))
def square_digits(num):
    st = []

    for i in str(num):
        int_i = int(i)
        sq_i = int_i**2
        st.append(str(sq_i))

    return int("".join(st))

#highest and lowest
def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"

#list filtering 
def filter_list(l):
    return [item for item in l if type(item) == int]