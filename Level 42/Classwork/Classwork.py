dict1 = {
    "name": "გიორგი",
    "surname": "შარია",
    "academy": "GOA",
    "fav-color": "ლურჯი",
    "city": "თბილისი",
    "goa-student": True,
    "age": 15,
    "fav-programming-lang": "Python"
}

print(dict1["name"])
print(dict1["surname"])
print(dict1["academy"])
print(dict1["fav-color"])
print(dict1["city"])
print(dict1["goa-student"])
print(dict1["age"])
print(dict1["fav-programming-lang"])



my_dict = {
    "apple": 2,
    "banana": 3,
    "goa": 5,
    "date": 4,
    "pirv": 1
}

print("Keys in dictionary:")
print(my_dict.keys())

print("Values in  dictionary:")
print(my_dict.values())

print("Key-Value in  dictionary:")
print(my_dict.items())


print("Iterating over the dictionary:")
for key, value in my_dict.items():
    print(f"The value for '{key}' is {value}.")