#davaleba pirveli

def welcome_text(name, age):
    return f"Welcome {name}. You are {age} years old."

name = input("Please input ur name: ")
age = input("Please input ur age: ")
print(welcome_text(name, age))

#davaleba meore
def format_name(first_name, last_name):
    print(f"{first_name.capitalize()} {last_name.capitalize()}")

first_name = input("Please input ur name: ")
last_name = input("Please input ur lastname: ")
format_name(first_name, last_name)

#davaleba mesame
def reverse_and_format(string):
    reversed_string = string[::-1]
    print(f"The reversed string is: {reversed_string}")

input_string = "GOA IS THE BEST"
reverse_and_format(input_string)

#davaleba meotxe

def insert_word_into_sentence(sentence, word, index):
    sentence_list = sentence.split()
    sentence_list.insert(index, word)
    print(sentence_list)

sentence = "I love programming"
word = "Python"
index = 2
insert_word_into_sentence(sentence, word, index)

#davaleba mexute

def sentence_to_word_list(sentence):
    print(sentence.split())

sentence = "This is a test text"
print(sentence_to_word_list(sentence))

#davaleba meeqvse
def csv_to_list(csv_string):
    print(csv_string.split(','))

csv_string = "apple,orange,goa,programming,hello!"
csv_to_list(csv_string)

#davaleba meshvide
def period_split_to_list(paragraph):
    print(paragraph.split("."))

period_split_to_list("This paragraph. is being seperated. by. periods")

#davaleba merve
def append_item_to_list(my_list, item):
    my_list.append(item)

my_list = [1, 2, 3]
item = 4
append_item_to_list(my_list, item)
print(my_list)

#davaleba mecxre

def append_items_to_list(original_list, items):
    for i in items:
        original_list.append(i)

original_list = [1, 2, 3]
items = [4, 5, 6]
append_items_to_list(original_list, items)
print(original_list)

#davaleba meate
def append_all_elements(list1, list2):
    for i in list2:
        list1.append(i)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
append_all_elements(list1, list2)
print(list1)

#davaleba metertmete
def insert_item_at_index(my_list, index, item):
    my_list.insert(index, item)

my_list = [1, 2, 3, 4]
index = 2
item = 10
insert_item_at_index(my_list, index, item)
print(my_list)

#davaleba metormete
def insert_item_at_beginning(my_list, beginning_item):
    my_list.insert(0, item)
    print(my_list)

my_list = [2, 3, 4]
beginning_item = 1
insert_item_at_beginning(my_list, beginning_item)

#davaleba mecamete
def insert_item_at_last(my_list, final_item):
    my_list.insert(len(my_list), item)
    print(my_list)


my_list = [2, 3, 4]
final_item = 5
insert_item_at_last(my_list, final_item)


