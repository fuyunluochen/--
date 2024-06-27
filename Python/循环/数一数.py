name = input("请输入字符串:")
查询 = input("请输入你想查询的字符:")
count1 = sum(x == 查询 for x in name)
print(f"{name}中一共有{count1}个{查询}")
