# 1)
numbers = [x for x in range(1, 11)]

# 2) 
squares = [x**2 for x in range(1, 6)]

# 3)
evens = [x for x in range(1, 21) if x % 2 == 0]

# 4)
words = ["apple", "GOA", "lalay", "today"]
first_letters = [word[0] for word in words]

# 5)
uppercase_words = [word.upper() for word in words]

# 6)
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]

# 7)
long_words = [word for word in words if len(word) > 4]

# 8)
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(x * 9/5) + 32 for x in celsius]

# 9)
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

# 10)
sentence = "GOA is the best programming academy mmm n"
vowel_words = [word for word in sentence.split() if any(v in word for v in 'aeiou') and len(word) > 5]

# 11)
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, 20)]
