class Phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，4G使用中")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
