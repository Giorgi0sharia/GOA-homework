name = "Giorgi"
# name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "Giorgi" არის ცვლადისთვის მნიშვნელობა
surname = "Sharia"

print(name)

# პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი
# name = "Giorgi" ეს არის str(string) ტიპის ცვლადი
# სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
age = 15 #  ეს არის int(integer) ტიპის ცვლადი მთელი რიცხვი
height = 1.75 # ეს არის float ტიპის ცვლადი ათწილადი
knows_programming = True # True or False
#ეს არის Bool(Boolean) ტიპის ცვლადი
print(name + " " + surname)
print(name, surname)
print(name + str(age))


print(type(name))
print(type(surname))
print(type(age))
print(type(height))
print(type(knows_programming))

# print(type(age)) - age გადაეცა type ფუნქციას, რომელმაც დააბრუნა მისი ტიპი
# და დაბრუნებული ნებისმიერი სიტყვა დავპრინტეთ, რომელმაც გაგვაგებინა, რომ
# print(type(age)) - ის ტიპი არის int(integer) - მთელი რიცხვი