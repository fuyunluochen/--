my_str = "奖1励鸡叫野马ss"
value1 = my_str[2]
value2 = my_str[-2]
print(value1, value2)


# index查找下标
value1 = my_str.index("s")
print(value1)


# replace方法替换指定字符生成新字符串
new_my_str = my_str.replace("ss", "面包")
print(new_my_str)


# split方法分割字符串
my_str = "奖励 鸡叫 野马 面包"
my_str_list = my_str.split(" ")
print(f"将{my_str}通过split方法进行分割后得到:{my_str_list},类型是:{type(my_str_list)}")
