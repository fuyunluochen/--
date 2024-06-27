# 简单if嵌套
print("欢迎来到坤坤动物园")
if int(input("请输入你的身高：")) > 120:
    print("你的身高大于120cm,不可以免费")
    print("不过如果你的VIP等级大于3则可以免费游玩")
    if int(input("请输入你的VIP等级:")) > 3:
        print("恭喜您，可以免费游玩")
    else:
        print("sorry,您需要补票,10元")
else:
    print("小朋友，欢迎你")

#
if 30 > int(input("请输入你的年龄")) >= 18:
    if int(input("你的入职时间是：")) > 2:
        print("可以领取")
    elif int(input("你的级别是：")) > 3:
        print("可以领取")
    else:
        print("不可以领取")
else:
    print("年龄不符合,不可以领取")

# 外层：表白100天
# 内层：每天10枝玫瑰花
i = 1
while i < 100:
    print(f"今天是第{i}天,准备表白")
    for j in range(1, 11):
        print(f"送给小美{str(j)}枝玫瑰花")
    print("小美,我喜欢你")
    i += 1
print(f"坚持到{i}天,表白成功")
