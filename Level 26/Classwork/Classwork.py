def greet(name):
  print("გამარჯობა" , name )

greet(input("Please inpur your name:"))



def manual_range(start, end, step):
  for i in range(start, end, step):
    if i % 2 == 0:
      print(i)

manual_range(1, 310, 1)
manual_range(5, 230, 2)
manual_range(120, 310, 3)
manual_range(0, 15, 5)
manual_range(-10, 150, 2)


def manual_len(my_list):
  count = 0
  for item in my_list:
    count += 1
  print("სიის სიგრძე:", count)

manual_len([1,456,89765,2,7,2,3])