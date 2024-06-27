# 两个数的和确定下一个数
a, b = 0, 1
while b < 100:
    print(b, end=",")
    a, b = b, a + b
