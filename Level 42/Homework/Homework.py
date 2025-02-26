#pirveli davaleba

my_dict = {'name': 'giorgi', 'age': 15, 'city': 'tbilisi', 'hobby': 'Reading'}
print(my_dict.keys())

#meore davaleba
print(my_dict.values())

#mesame davaleba
print(my_dict.items())

#meotxe davaleba
for key, value in my_dict.items():
    print(f'{key}: {value}')

#mexute davaleba
def check_a_key(key_to_check):
    if key_to_check in my_dict:
        print(f'{key_to_check} exists in the dictionary.')
    else:
        print(f'{key_to_check} does not exist in the dictionary.')

check_a_key("city")

#meeqvse davaleba
my_dict2 = {'name': 'giorgi', 'age': 15}
my_dict2['city'] = 'tbilisi'
print(my_dict2)

#meshvide davaleba
my_dict2.pop('age')
print(my_dict2)

#merve davaleba
new_info = {'color': 'yellow', 'hobby': 'GOA'}
my_dict2.update(new_info)
print(my_dict2)

#mecxre davaleba
print(len(my_dict2))

#meate davaleba
def sum_numeric_values(my_dict):
    return sum(v for v in my_dict.values() if type(v) == int or type(v) == float)

my_dict3 = {'a': 10, 'b': 20, 'c': 'Hello', 'd': 5}
print(sum_numeric_values(my_dict3))

#metertmete davaleba
my_dict3.clear()
print(my_dict3)

#metormete davaleba
my_info = {
    'name': 'giorgi',
    'surname': 'sharia',
    'age': 15,
    'city': 'tbilisi',
    'hobby': 'GOA',
    'favorite_color': 'Blue',
    'languages_spoken': ['English', 'georgian'],
    'is_online': True,
    'height': 1.78,
    'favorite_food': 'xachapuri'
}
print(my_info)