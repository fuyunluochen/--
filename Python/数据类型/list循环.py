my_list = ["叽叽哥", "奖励哥", "面包哥", "快猫哥"]
my_list2 = ["4", "3", "2", "1"]


def list_while(x):

    index = 0
    while index < len(x):
        print(x[index])
        index += 1


def list_for(x):
    index = 0
    for i in x:
        print(i[index])


list_while(my_list)
list_while(my_list2)
list_for(my_list2)
