
#codewars

#Beginner Series #2 Clock
def past(h, m, s):
    sum_of_seconds = 0
    result = sum_of_seconds * 1000
    return result

#A Needle in the Haystack
def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"

#Invert values
def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list

#calculate averadge
def find_average(numbers):
    if numbers == []: return 0
    return sum(numbers) / len(numbers) 

#Sentence Smash
def smash(words):
    return " ".join(words)

#Beginner - Reduce but Grow
def grow(arr):
    product = 1

    for i in arr:
        product *= i

    return product

#Is he gonna survive?
def hero(bullets, dragons):
    if bullets >= dragons * 2: return True
    return False

#How good are you really?
def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)

    if your_points > other_avg: return True
    return False

#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    counter = 0
    sum_negative = 0
    for i in arr:
        if i > 0:
            counter += 1 
        elif i < 0:
            sum_negative += i
    result = [counter,sum_negative]
    if result != [0,0]:
        return result
    return [0,0]

#DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace("T", "U")

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    return False

#Calculate BMI
def bmi(weight, height):
    bmi_value = weight / height ** 2

    if bmi_value <= 18.5: return "Underweight"
    elif bmi_value <= 25.0: return "Normal"
    elif bmi_value <= 30.0: return "Overweight"
    return "Obese"

#Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

#Fake Binary
def fake_bin(x):
    final=""
    for i in x:
        if int(i) < 5:
            final+="0"
        else: final+="1"
    return final

#You only need one - Beginner
def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False

#Count by X
def count_by(x, n):
    result = []

    for i in range(1, n+1):
        result.append(x*i)

    return result

#reversed sequence
def reverse_seq(n):
    if n > 0:
        return list(range(n, 0, -1))

#rock paper scissors
def rps(p1, p2):
    if p1 == p2: return "Draw!"
    elif p1 == "scissors" and p2 == "paper": return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors": return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock": return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper": return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors": return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock": return "Player 2 won!"

#is n divisible by x and y?
def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    return False

#if you cant sleep, just count sheep!
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

#grasshopper - gradebook
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'