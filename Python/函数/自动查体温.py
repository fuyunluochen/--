def body_temperature(x):
    print("欢迎来到动物园!请出示您的健康码以及72小时核酸证明，并配合测量体温!")
    if x <= 37.5:
        print(f"体温测量中,您的体温是:{x}度,体温正常请进!")
    else:
        print(f"体温测量中,您的体温是:{x}度，需要隔离!")


body_temperature(float(input("请输入您的体温:")))
