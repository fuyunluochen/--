class Phone:
    IMEI = None
    prducer = "xiaomi"

    def call_by_5g(self):
        print("5G通话")


class NFCReader:
    nfc_type = "第5代"
    producer = "xiaomi"

    def read_card(self):
        print("读取NFC卡")

    def write_card(self):
        print("写入NFC卡")


class remotecontrol:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")


class myphone(Phone, NFCReader, remotecontrol):
    pass


myphone = myphone()
myphone.call_by_5g()
myphone.control()
print(myphone.producer)
