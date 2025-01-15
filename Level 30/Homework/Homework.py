#davaleba pirveli

sentence = "GOA IS THE BEST"
uppercase_sentence = sentence.upper()

# shedegi
print(uppercase_sentence)

#davaleba meore
name = input("please input your name: ")
upper_name = name.upper()

print(upper_name)

#davaleba mesame

def convert_to_uppercase_inplace(strings_list):
    for i in range(len(strings_list)):
        strings_list[i] = strings_list[i].upper()

lowercase_strings = ["hello", "world", "GOA", "programming"]
convert_to_uppercase_inplace(lowercase_strings)

print(lowercase_strings)

#davaleba meotxe
sentence2 = "tHiJDkoadjhKDJA"
lowercase_sentence2 = sentence2.lower()

print(lowercase_sentence2)

#davaleba mexute
email = input("Please enter your email address: ")
email = email.lower()

print("Your email address in lowercase is:", email)

#davaleba meeqvse
def convert_to_lowercase_inplace(mixed_case_string):
    mixed_case_string = mixed_case_string.lower()
    print(mixed_case_string)


mixed_string = "fjIWUFEijofeahouh8EHFUo"
convert_to_lowercase_inplace(mixed_string)

#davaleba shvidi
sentence3 = input("Please enter a sentence: ")

capitalized_sentence3 = sentence3.capitalize()

print(capitalized_sentence3)

#davaleba merve
strings_list = ["hello", "hi", "GOA", "programming"]
for i in range(len(strings_list)):
    strings_list[i] = strings_list[i].capitalize()

print(strings_list)

#davaleba mecxre
def capitalize_first_letter(input_string):
    input_string = input_string.capitalize()
    print(input_string)

sentence4 = "magaliti"
capitalize_first_letter(sentence4)

#davaleba meate
sentence5 = "I love programming in GOA. GOA IS BEST."

position = sentence5.find("GOA")
print(position)

#davaleba metertmete
substring = input("Enter the substring to search: ")
string = input("Enter the string to search: ")

position = string.find(substring)

print("The substring" ,substring," starts at index" ,position)

#davaleba metormete
def find_char_index(input_string, char):
    index = input_string.find(char)
    print(index)

string = "Hello programming is great in GOA"
character = "o"
find_char_index(string, character)

#davaleba mecamete
user_string = input("Enter a string: ")

print("The length of the string is:", len(user_string))

#davaleba metotxmete
def get_strings_lengths_inplace(strings_list):
    lengths = [0] * len(strings_list)
    
    for i in range(len(strings_list)):
        lengths[i] = len(strings_list[i])
    
    print(lengths)

strings = ["apple", "banana", "dog", "orange"]
get_strings_lengths_inplace(strings)

#davaleba metxutmete
paragraph = "The dog is smart, but the cat is smarter. the children are outside"

the_count = paragraph.count("the")

print("The word 'the' appears", the_count, "times.")

#davaleba meteqvsmete
text = "hello, how are you today?"

char = input("Enter a character to count how many there is: ")

char_count = text.count(char)

print("The character", char," appears", char_count, "times in the string.")

#davaleba metvramete
paragraph2 = input("Input a paragraph; ")
user_inputted_word = input("Input a word to search in ur paragraph: ")

specific_word_count = paragraph.count(user_inputted_word)

print("The word", user_inputted_word, "appears", specific_word_count, "times.")

#davaleba mecxramete
text = "hello. how are you today. hello"

print(text.find("hello"))

#davaleba meoce
def find_char_index(string, char):
    print(string.find(char))

user_string = input("Enter a string: ")
user_char = input("Enter a character to find its index in ur string: ")

find_char_index(user_string, user_char)

#davaleba ocdaerti
text2 = "hello"

print(text2.islower())

#davaleba ocdaori
def check_lowercase(string):
    print(string.islower())

check_lowercase(input("Enter a string: "))

#davaleba ocdasami
text = input("Enter a string: ")

print(text.isupper())

#davaleba ocdaotxi
text = input("Enter a string: ")

print(text.isupper())

#davaleba ocdaxuti
def check_uppercase(string):
    print(string.isupper())

check_uppercase(input("Enter a string: "))

#davaleba ocdaqvsi
user_input = input("Enter a string: ")

print(user_input.isupper())

#davleba ocdashvidi
sentence6 = "The dog chased the cat. cat dog cat dog"

print(sentence6.replace("dog", "cat"))

#davaleba ocdarva
def replace_spaces_with_underscores(string):
    print(string.replace(" ", "_"))

replace_spaces_with_underscores(input("Enter a string: "))

#davaleba ocdacxra
sentence7 = input("Enter a string: ")

print(sentence7.swapcase())

#davaleba ocdaati
def swap_case(sentence):
    print(sentence.swapcase())

swap_case(input("Enter a string: "))
#a