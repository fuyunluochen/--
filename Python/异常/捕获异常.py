# 基本捕获异常
# try:
#     open("cc.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常，将更换文件打开模式")
#     open("cc.txt", "w", encoding="UTF-8")

# 捕获指定异常
# try:
#     print(Name)
#     # 1/0
# except NameError as e:
#     print("出现未被定义的异常")
#     print(e)

# 捕获多个异常
# try:
#     print(1 / 0)
#     print(Name)
# except (NameError, ZeroDivisionError) as e:
#     print('ZeroDivision错误...')
#     print("出现啦未定义多变量或者除以零异常")

# 捕获全部异常
# try:
#     text = open("hh", "r", encoding="UTF-8")
# except Exception as e:
#     print("出现异常")
# 没有异常

try:
    f = open("111.txt", "r", encoding="UTF-8")
except:
    print("出现异常")
    f = open("111.txt", "w", encoding="UTF-8")
else:
    print("好高兴，没有出现异常")
#finally有没有异常都会执行
finally:
    f.close()
