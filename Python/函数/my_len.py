str1 = "sdfkhbcvmn"
str2 = "akfbkaf b"
str3 = "sjgvbjnfb"


def my_len(date):
    count = 0
    for i in date:
        count += 1
    print(f"字符串{date}的长度是:{count}")


my_len(str1)
my_len(str2)
my_len(str3)
