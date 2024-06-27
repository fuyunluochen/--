def user_info(name, age, gender):
    print(f"您的姓名是:{name},年龄是:{age},性别是:{gender}")


# 位置传入参数
user_info("小明", 20, "男")
# 关键字传入参数
user_info(name="小红", age=18, gender="女")
# 混合传入参数
user_info("晓晓", age=16, gender="女")


# 缺省参数
def user_info1(name, age, gender="女"):
    print(f"您的姓名是:{name},年龄是:{age},性别是:{gender}")


user_info1("潇潇", 20)
user_info1("小壮", 18, "男")


# 不定长位置传参
def user_info2(*args):
    print(args)


user_info2("Tom", 10, "男")


# 不定长关键字传参
def user_info3(**kwargs):
    print(kwargs)


user_info3(name="鸡鸡哥", age=17, gender="男")
