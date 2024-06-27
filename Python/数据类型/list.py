my_len = ["tom", "Lily", "Rose"]
# 小标索引取值
print(my_len[0])
print(my_len[1])
print(my_len[2])


# 反向下标取值
print(my_len[-1])
print(my_len[-2])
print(my_len[-3])


# 嵌套列表
my_len = [[1, 2, 3], [4, 5, 6]]
print(my_len[1][0])


# list.index方法
index = my_len.index("Lily")
print(index)

# list修改元素
my_len[0] = "python"
print(my_len[0])


# list插入元素
insert = my_len.insert(0, "hello")
print(my_len)

# list.append追加元素
append = my_len.append("奖励哥")
print(my_len)


# list.extend追加元素
my_len2 = [
    1,
    2,
    3,
]
my_len.extend(my_len2)
print(my_len)


# del pop方法删除元素
del my_len[0]
my_len.pop(0)
print(my_len)


# remove方法删除元素
my_len.remove("tom")
print(my_len)


# clear方法清空列表
my_len.clear()
print(my_len)


# count 方法统计指定元素数量

my_len3 = [1, 1, 1, 2, 1, 3, 1, 54, 1, 1]
print(my_len3.count(1))


# len 函数统计列表所有元素
print(len(my_len))
