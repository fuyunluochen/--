class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__内置方法
    def __str__(self):
        return f"Student类对象,name:{self.name},age:{self.age}"

    # __lt__内置方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__内置方法
    def __le__(self, other):
        return self.age <= other.age


stu1 = Student("奖励哥", 18)
stu2 = Student("叽叽哥", 18)
print(stu1 <= stu2)
print(stu1 >= stu2)
# print(stu)
# print(str(stu))
