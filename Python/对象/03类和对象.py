class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


Clock1 = Clock()
Clock1.id = "001"
Clock1.price = 9.9
print(f"闹钟编号是{Clock1.id},价格为{Clock1.price}")
Clock1.ring()
