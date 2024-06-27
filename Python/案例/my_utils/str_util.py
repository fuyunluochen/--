def str_reverse(s):
    """
    将获取的字符串反转后输出
    :param s:字符串
    :print:反转后的字符串
    """
    print(s[::-1])


def substr(s, x, y):
    """
    将字符串切片
    :param s:字符串
    param x:切片的开始下标
    param y:切片的结束下标
    """
    str = s[int(x):int(y):1]
    print(str)
