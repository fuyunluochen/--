# {key: value, key: value, key: value}
# my_dict1={key: value, key: value, key: value}
# my_dict2={}
# my_dict3=dict()
# print(f"{type(my_dict2)}")
# stu_score = {"奖励哥": 99, "叽叽哥": 88, "面包哥": 77, "快猫哥": 66}
# print(stu_score[input("请输入您要查询的名称:")])


#
stu_score_dict = {
    "奖励": {"语文": 77, "数学": 66, "英语": 33},
    "鸡鸡": {"语文": 77, "数学": 66, "英语": 33},
    "面包": {"语文": 77, "数学": 66, "英语": 33},
}
# 查询成绩
# print(stu_score_dict[input("请输入您要查询的名称:")][input("请输入您要查询的学科:")])


# 新增元素
stu_score_dict["快猫"]={"语文":55,"数学":66,"英语":45}
print(stu_score_dict)


# 更改元素
stu_score_dict["奖励"] = {"语文": 100, "数学": 100, "英语": 100}
print(f"字典更新后为:{stu_score_dict}")


# pop删除元素
value=stu_score_dict.pop("快猫")
print(value)
print(stu_score_dict)


# clear清空字典
# stu_score_dict.clear()
# print(f"字典被清空了，内容是：{stu_score_dict}")


# 获取全部的key
keys=stu_score_dict.keys()
# print(keys)


# 遍历循环
# 方法1：通过获取字典全部的key值来完成遍历
for key in keys:
    print(f"字典的key值是:{key}")
    print(f"字典的value是:{stu_score_dict[key]}")
# 方法2：直接对字典进行for循环，每一次循环都直接得到key
for key in stu_score_dict:
    print(f"字典的值是:{key}")
    print(f"字典的value是:{stu_score_dict[key]}")
