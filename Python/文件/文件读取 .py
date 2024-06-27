import time
with open("测试.txt", "r", encoding="UTF-8") as file_manipulation:
    print(type(file_manipulation))

    # read方法读取文件文件指定字节长度
    print(f"read方法读取4个字节：{file_manipulation.read(4)}")
    print(f"rean方法读取全部字节：{file_manipulation.read()}")
    print(f"read方法获取都数据数据类型是：{type(file_manipulation)}")

    # readlines方法读取文件全部内容
    content = file_manipulation.readlines()
    print(f"readlines方法类型是：{type(content)}")
    print(f"readlines方法获取文件全部行：{content}")

    for j, i in enumerate(file_manipulation, start=1):
        print(f"第{j}行，内容是：{i}")
with open("测试.txt", "r", encoding="UTF-8") as f:
    for i in f:
        print(f"{i}")
time.sleep(50000)
