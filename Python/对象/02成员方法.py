class Student:
    name = None

    def say_hi(self):
        print(f"大家好呀，我是{self.name},请大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")


stu_1 = Student()
stu_1.name = "奖励"
stu_1.say_hi()

stu_2 = Student()
stu_2.name = "鸡"
stu_2.say_hi2("你干嘛哎呦")