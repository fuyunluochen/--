class Phone:
    IMEI = None
    producer = "小米"  # 厂商

    def call_by_5g(self):
        print("小米5g已开启")


class MyPhone(Phone):
    producer = "红米"  # 复写弗雷成员变量

    def call_by_5g(self):
        print("红米5g已开启")
        # 使用父类的方式一
        print(f"父类的厂商是{Phone.producer}")
        Phone.call_by_5g(self)
        # 使用父类的方式二
        print(f"父类的厂商名是:{super().producer}")
        super().call_by_5g()


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
