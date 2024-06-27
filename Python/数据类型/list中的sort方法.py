my_list = [["a", 33], ["b", 44], ["c", 55]]


def choose_sort_key(element):
    return element[1]


my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)


my_list.sort(key=lambda element: element[1], reverse=True) 