# 对形参进行类型注解
def add(x: int, y: int):
    return x + y


add(1, 2)


# 对返回值进行注解
def func(data: list) -> list:
    return data


print(func(1))
