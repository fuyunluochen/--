# sourcery skip: identity-comprehension, set-comprehension
my_list = [
    "黑马程序员", "传智教育", "黑马程序员", "传智教育", "itheima", "itcast", "itheima", "itcast",
    "best"
]
my_set = set()
for i in my_list:
    my_set.add(i)
print(f"列表{my_list}\n去重后的集合为:{my_set}")