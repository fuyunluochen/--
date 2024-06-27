my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list_while(x):
    my_list2 = [x[index] for index in range(len(x)) if int(x[index]) % 2 == 0]
    print(f"使用while循环从列表:{x}中取出偶数,组成新列表:{my_list2}")


def list_for(x):
    index = 0
    my_list2 = [i for i in x if int(i) % 2 == 0]
    print(f"使用for循环从列表:{x}中取出偶数,组成新列表:{my_list2}")


list_while(my_list)
list_for(my_list)
