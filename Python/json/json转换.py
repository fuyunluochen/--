import json
# 嵌套字典转json
date = [
    {
        "name": "奖励哥",
        "age": 18
    },
    {
        "name": "面包哥",
        "age": 18
    },
    {
        "name": "鸡鸡哥",
        "age": 18
    },
]
json_str1 = json.dumps(date, ensure_ascii=False)
print(type(json_str1))
print(json_str1)
# 字典转json
d = {"name": "周杰轮", "addr": "台北"}
json_str2 = json.dumps(d, ensure_ascii=False)
print(type(json_str2))
print(json_str2)
#
s = '{"name": "周杰轮", "addr": "台北"}'
d=json.loads(s)
print(f"{type(d)}{d}")
