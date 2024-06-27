def test_function(compute):
    result = compute(int(input("请输入x：")), int(input("请输入y：")))
    print(result)
    print(f"compute函数的类型是:{type(compute)}" )


def compute_jia(x, y):
    return x+y


def compute_jian(x, y):
    return x-y


# test_function(compute_jian)
test_function(lambda x, y: x+y)
