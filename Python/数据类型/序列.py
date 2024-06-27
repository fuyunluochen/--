# 对列表进行切片
my_list = [1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]
print(f"对列表进行切片: {result1}")


# 对元组进行切片
my_tuple = (1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(f"对元组进行切片: {result2}")


# 对字符串进行切片
my_str = "0123456789"
result3 = my_str[9:0:3]
print(f"对字符串进行切片:{result3}")


# 对字符串进行反向切片
result3=my_str[::-3]
print(f"对字符串进行反向切片:{result3}")


# 对元组进行反向切片
result2=my_tuple[5:1:-2]
print(f"对元组进行反向切片:{result2}")


# 对列表进行反向切片
result1=my_list[::-4]
print(f"对列表进行反向切片:{result1}")
