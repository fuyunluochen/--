from time import *  #使用*导入全部功能

sleep(5)
print("Hello World")

from time import sleep  #使用from 模块名 import 函数导入某一函数

sleep(5)
print("Hello World")

import time  #import 模块名导入全部内容

sleep(5)
print("Hello World")

import time as t  #as给特定对象赋予别名

t.sleep(5)
print("Hello World")

# # 导入自定义模块
from 自定义模块 import *

test_b()

# 导入Python包
from my_package import my_module1
from my_package import my_module2

my_module1.info_print1()
my_module2.info_print2()
