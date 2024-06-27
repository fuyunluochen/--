import random
num = random.randint(1, 100)
# 嵌套if猜数子
数值 = int(input("请输入你猜出的值：(大于1小于10)"))
if 数值 == num:
    print("恭喜,第一次就猜出来了")
elif 数值 > num:
    print("真遗憾,猜大了哦")
else:
    print("真遗憾,猜小了哦")
数值 = int(input("请输入你猜出的值：(大于1小于10)"))
if 数值 == num:
    print("恭喜,第二次就猜出来了")
elif 数值 > num:
    print("真遗憾,猜大了哦")
else:
    print("真遗憾,猜小了哦")
数值 = int(input("请输入你猜出的值：(大于1小于10)"))
if 数值 == num:
    print("恭喜,第三次就猜出来了")
elif 数值 > num:
    print("真遗憾,猜大了哦")
else:
    print("真遗憾,猜小了哦")
print(f"答案为{num}", "你猜对了吗？")

# while 猜数字
count = 0
while True:
    guess_num = int(input("请输入你猜测的值："))
    count += 1
    if guess_num == num:
        print("恭喜你，猜中了")
        break
    elif guess_num > num:
        print("你猜的数大了")
    else:
        print("你猜的数小了")
print(f"您总共猜测了{str(count)}次")
