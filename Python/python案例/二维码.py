import pyqrcode
# 设置二维码信息
s = "https://www.bilibili.com"
# 生成二维码
url = pyqrcode.create(s)
# 生成二维码文件
url.svg("bilibili.svg",scale=8)

