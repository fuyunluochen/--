import my_utils.file_util
import my_utils.str_util

my_utils.str_util.str_reverse(input("请输入字符串："))
my_utils.str_util.substr(input("请输入字符串："), input("请输入起始位置："),input("请输入终止位置："))

my_utils.file_util.print_file_info("cc.txt")
my_utils.file_util.append_to_file(input("请输入文件名："), input("请输入内容："))
