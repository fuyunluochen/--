class Student:
    # name = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")


stu = Student("奖励", 18, "177********")
print(stu.name)
print(stu.age)
print(stu.tel)
