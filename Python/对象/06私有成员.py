class phone:
    IMEI = None  # 序列号
    producer = None  # 厂商
    __Electric_quantity = 19  # 当前电量

    def call_by_5g(self):
        if self.__Electric_quantity >= 20:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足,已开启省电模式")

    def __keep_single_core(self):
        print("电量不足")


phone = phone()
phone.call_by_5g()
