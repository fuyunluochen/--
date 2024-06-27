import random

Account_balance = 10000
for i in range(1, 21):
    performance = random.randint(1, 10)
    if performance > 5:
        Account_balance -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{Account_balance}元")
    else:
        print(f"员工{i},绩效分{performance},低于5,不发工资，下一位")
    if Account_balance == 0:
        break
print("工资发完了，下个月领取吧")
