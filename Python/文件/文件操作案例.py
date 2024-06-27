with open("文件操作案例.txt", "r", encoding="UTF-8") as text:
    for i in text:
        if i.count("测试") > 0:
            continue
        with open("bill.txt.bak", "a", encoding="UTF-8") as w:
            w.write(i)
   
   