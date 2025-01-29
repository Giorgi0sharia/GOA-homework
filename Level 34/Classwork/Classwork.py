def remove_elements_by_indexes(main_list, indexes_list):

    for i in sorted(indexes_list, reverse=True):  
        if 0 <= i < len(main_list):
            main_list.pop(i)


def remove_one_element(main_list, index):
    if 0 <= index < len(main_list):  
        main_list.pop(index)  
    print(main_list)  