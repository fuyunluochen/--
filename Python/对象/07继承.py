class Phone2018():
    IMEI = None
    producer = None

    def call_by_4g(self):
        print("4G通话")


class Phone2023(Phone2018):  # 继承
    face_id = "10086"

    def call_by_5g(self):
        print("5G通话")


phone2023 = Phone2023()
print(phone2023.producer)
phone2023.call_by_4g()
phone2023.call_by_5g()
