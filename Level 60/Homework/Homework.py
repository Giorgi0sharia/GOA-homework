#the wide-mouthed frog
def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'

#Get Nth Even Number
def nth_even(n):
    return (n - 1) * 2

#Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
def replace_exclamation(s):
    return ''.join('!' if c.lower() in 'aeiou' else c for c in s)

#5 without numbers !!
def unusual_five():
    return len("apple")

#Add Length
def add_length(s):
    return [f"{word} {len(word)}" for word in s.split()]