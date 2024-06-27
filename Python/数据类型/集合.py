# 单纯集合
# {"奖励", "叽叽", "斑马", "面包"}
# 空集合
my_set = set()
# 集合
my_animal_friend = {"奖励", "叽叽", "斑马", "面包"}
print(f"my_animal_friend的内容是:{my_animal_friend},类型是:{type(my_animal_friend)}")


# add添加元素
my_animal_friend.add("快猫")
print(my_animal_friend)


# remove 移除元素
my_animal_friend.remove("面包")
print(my_animal_friend)


# pop 移出元素
element = my_animal_friend.pop()
print(my_animal_friend)
print(element)


# clear清空集合
my_animal_friend.clear()
print(my_animal_friend)


# difference 计算两个集合之间的差集
set1 = {1, 3, 5}
set2 = {1, 4, 6}
set3 = set1.difference(set2)
print(f"{set1}与{set2}之间的差集为:{set3}")


# difference_update 方法消除2个集合的差集
set1 = {1, 3, 5}
print(f"原集合1的值为:{set1}")
set2 = {1, 4, 6}
set1.difference_update(set2)
print(f"集合1的值为:{set1}\n集合2的值为:{set2}")


# union 合并集合
set1 = {1, 3, 5}
set2 = {2, 4, 6}
set3 = set1.union(set2)
print(f"集合1与集合2合并后的集合为:{set3}")


# len 统计集合元素个数
set1={1,2,3,4,5}
print(f"集合总共有{len(set1)}个元素")


# 集合遍历
set1 = {1, 2, 3, 4, 5}
for i in set1:
    print(f"集合的元素有:{i}")
