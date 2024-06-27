# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: str = "鸡"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()
# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, "hello", True)
my_dict: dict = {"hello": 123}
# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "hello", True)
my_dict: dict[str, int] = {"hello": 123}
# 在注释中进行类型注解
var_1 = random.randint(0, 10)  # type: int
var_2 = json.loads({"name": "zhangsan"})  # type: dict[str,str]


def func():
    return 10


var_3 = func()  # type:ints
