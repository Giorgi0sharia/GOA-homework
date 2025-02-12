#davaleba 1

my_tuple = (10, 20, 30, 40, 50)

second_element = my_tuple[1]

last_element = my_tuple[-1]

middle_element = my_tuple[1:4]

print("Second element:", second_element)
print("Last element:", last_element)
print("Middle three elements:", middle_element)


#davaleba 2

#my_tuple = (10, 20, 30)

#my_tuple[1] = 50  

#print(my_tuple)

#erroria

#davaleba 3

my_tuple = (10, 'apple', 3.14, True)

integer_value, string_value, float_value, boolean_value = my_tuple 

# Print each variable
print("Integer value:", integer_value)
print("String value:", string_value)
print("Float value:", float_value)
print("Boolean value:", boolean_value)

#davaleba 4

my_tuple = (10, 20, 30, 10, 40, 10)

count_10 = my_tuple.count(10)

first_10 = my_tuple.index(10)

print("Count of 10:", count_10)
print("First occurrence of 10 is at index:", first_10)

#davaleba 5



my_set = {10, 20, 30, 40, 50}


my_set.add(60)


my_set.remove(20)


def is_value_present(value, my_set):
    for i in my_set:
        if i == value:
            return True
    return False

is_30_present = is_value_present(30, my_set)
is_100_present = is_value_present(100, my_set)

print("Is 30 present in the set?", is_30_present)
print("Is 100 present in the set?", is_100_present)

#davaleba 6

set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 60, 70, 80}

union_set = set_a.union(set_b)  

intersection_set = set_a.intersection(set_b) 

difference_set = set_a.difference(set_b)  

print("Union of set_a and set_b:", union_set)
print("Intersection of set_a and set_b:", intersection_set)
print("Difference (set_a - set_b):", difference_set)

#davaleba 7

my_list = [10, 20, 30, 20, 40, 30, 50, 50]

set1 = set(my_list)

list2 = list(set1)

print("Original list:", my_list)
print("List after removing duplicates:", list2)