my_lit = []


class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, afe, address):
        self.name = name
        self.age = afe
        self.address = address
        my_lit.append((name, afe, address))


for i in range(10):
    print(f"当前录入第{i + 1}为学生信息，总共需录入10位学生信息")
    stu = Student(input("请输入学生姓名:"), int(input("请输入学生年龄:")), input("请输入学生地址:"))
    print(f"学生{i + 1}信息录入完成，信息为:[学生姓名:{stu.name},年龄:{stu.age},地址:{stu.address}]")
print(my_lit[9])
