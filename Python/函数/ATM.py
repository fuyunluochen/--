def main():
    print(f"{name},您好,欢迎来到ikunATM。请选择操作:\n"
          f"查询余额\t[输入1]\n"
          f"存款\t\t[输入2]\n"
          f"取款\t\t[输入3]\n"
          f"退出\t\t[输入4]\n"
          )
    return input("请选择您想办理的业务:")


def check_your_balance(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f'{name},您好，您当前账户余额剩余{money}元')


def deposit(num1):
    print("----------存款----------")
    global money
    money += num1
    print(f"{name},您好,存入{num1}元成功")
    check_your_balance(False)


def withdraw_money(num2):
    print("----------取款----------")
    global money
    money -= num2
    print(f"{name},您好,取款{num2}元成功")
    check_your_balance(False)


money = 500000
name = input("请输您的姓名:")
while True:
    num10 = main()
    if num10 == "1":
        check_your_balance(True)
        continue
    elif num10 == "2":
        num1 = int(input("请输入存入金额:"))
        deposit(num1)
        continue
    elif num10 == "3":
        num2 = int(input("请输入取款金额:"))
        withdraw_money(num2)
        continue
    else:
        print("程序结束啦")
