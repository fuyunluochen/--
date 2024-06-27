# 异常具有传递性
def function1():
    print("这是function1开始")
    num = 1 / 0  # 出现除零异常没有被捕获
    print("这是function结束")


def function2():
    print("这是function2开始")
    function1()  # 调用function1继承异常的同时没有捕获异常
    print("这是function2结束")


def mian():
    try:
        function2()  # 通过try调用function2的同时捕获异常
    except Exception as e:
        print("出现异常")
        print(e)


mian()
