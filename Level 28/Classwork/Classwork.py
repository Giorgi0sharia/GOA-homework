def manual_index(main_string, search_string):
  
  for i in range(len(main_string)):
    if main_string[i:i + len(search_string)] == search_string:
      print(search_string ,'არის',main_string,' ში ',i ,"ინდექსზე.")
    else:
        print(search_string,'არ არის',main_string,' ში.')

manual_index("ARMY","A")