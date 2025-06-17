# 1. Validate a PIN code
def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)


# 2. Is this a triangle?
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


# 3. Duplicate Encoder
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(char) == 1 else ')' for char in word)


# 4. Division of the integers into odd and even
def open_or_senior(data):
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]


# 5. Find the next perfect square
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return int((root + 1) ** 2)
    return -1

if __name__ == "__main__":

    print(validate_pin("1234"))  
    print(validate_pin("12345")) 

    print(is_triangle(3, 4, 5))
    print(is_triangle(1, 2, 3))


    print(duplicate_encode("Success"))


    print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))  


    print(find_next_square(121))  
    print(find_next_square(114))  
