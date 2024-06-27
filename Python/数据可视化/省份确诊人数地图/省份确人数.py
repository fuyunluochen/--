import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("数据可视化/省份确诊人数地图/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"][3]["children"]
data_list = []
for city_data in province_data_list:
    if city_data["name"] == "济源示范区":
        city_data["name"] = "济源"
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))
# 构建地图
map = Map()
map.add("河南省疫情分布", data_list, "河南")
map.set_global_opts(title_opts=TitleOpts(title="河南省疫情确诊人数图"),
                    visualmap_opts=VisualMapOpts(is_show=True,
                                                 is_piecewise=True,
                                                 pieces=[
                                                     {
                                                         "min": 1,
                                                         "max": 99,
                                                         "loble": "1~99人",
                                                         "color": "green"
                                                     },
                                                     {
                                                         "min": 100,
                                                         "max": 999,
                                                         "loble": "100~999人",
                                                         "color": "yellow"
                                                     },
                                                     {
                                                         "min": 1000,
                                                         "max": 9999,
                                                         "loble": "1000~9999人",
                                                         "color": "red"
                                                     },
                                                 ]))
map.render("河南省疫情确诊图.html")