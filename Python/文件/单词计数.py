with open("单词计数素材.txt", "r", encoding="UTF-8") as text:
    i = 0
    query = input("请输入您需要查询的值：")
    for line in text:
        j = line.count(query)
        i += j
    print(f"单词计数素材中总共有：{i}个{query}")
