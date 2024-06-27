my_str="itheima itcast boxuegu"
count=my_str.count(input("请输入要查找的字符:"))
print(f"{my_str}中一共有:{count}个字符")
my_str2=my_str.replace(" ","|")
print(f"{my_str}替换后为:{my_str2}")
Unknown=my_str2.split("|")
print(f"{my_str2}按|分割后为:{Unknown},其类型是:{type(Unknown)}")