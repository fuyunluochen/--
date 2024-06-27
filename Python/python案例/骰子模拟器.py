import random
min_val=1
mix_val=6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
    print("开始投骰子")
    print("骰子数值是:")
    # 第一轮
    print(random.randint(min_val,mix_val))
    # 第二轮
    print(random.randint(min_val,mix_val))
    # 是否继续
    roll_again=input("是否继续投骰子？(yes/no)")