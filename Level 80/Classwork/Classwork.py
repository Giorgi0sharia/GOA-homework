# ✅ 1. Find the stray number
def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num

# ✅ 2. Sort Numbers
def solution(nums):
    return sorted(nums) if nums else []

# ✅ 3. Find numbers divisible by a given number
def divisible_by(numbers, divisor):
    return [n for n in numbers if n % divisor == 0]

# ✅ 4. Detect Pangram
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(s.lower())

# ✅ 5. Counting Duplicates
def duplicate_count(text):
    text = text.lower()
    return len([char for char in set(text) if text.count(char) > 1])

