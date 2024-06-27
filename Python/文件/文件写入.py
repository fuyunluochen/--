import time
with open("单词计数素材.txt", "w",
          encoding="UTF-8") as text:  #open方法中w模式：无文件创建写，有文件覆盖写
    text.write("hello world!")
    # time.sleep(20)
    text.flush()
    for _ in range(10):
        with open("单词计数素材.txt", "a",
                  encoding="UTF-8") as text:  #open方法中a模式：无文件创建写，有文件追加写
            text.write("hello\n ")