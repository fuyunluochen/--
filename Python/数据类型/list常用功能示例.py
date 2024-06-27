my_list = [21, 25, 21, 23, 22, 20]
my_list.append(31)  
my_list.extend([29,33,30])
print(my_list.pop(0))
print(my_list.pop(-1))
count=my_list.index(31)
print(my_list,count)
