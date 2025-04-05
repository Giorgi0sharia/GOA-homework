
#Find the first non-consecutive number
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None 
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    
    return None 

#altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(s):
    return s.swapcase()

#Correct the mistakes of the character recognition software
def correct(text):
    # Dictionary of common OCR mistakes
    corrections = {
        '0': 'O',  # Misrecognizing 0 as O
        '1': 'I',  # Misrecognizing 1 as I
        '5': 'S',  # Misrecognizing 5 as S
        '8': 'B',  # Misrecognizing 8 as B
        'l': 'I',  # Misrecognizing l as I
    }
    corrected_text = ''.join([corrections.get(char, char) for char in text])
    return corrected_text

#IS IT A PALIDROME?
def is_palindrome(s):

    clean_string = ''.join(char.lower() for char in s if char.isalnum())
    
    return clean_string == clean_string[::-1]

#Do I get a bonus?
def bonus_time(salary, bonus):

    total_salary = salary * 10 if bonus else salary

    return f"${total_salary}"

#Student's Final Grade
def final_grade(exam, projects):
    # Check for the highest grade first
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
#Sum The Strings
def sum_strings(a, b):
    a_int = int(a) if a else 0
    b_int = int(b) if b else 0
    return str(a_int + b_int)

