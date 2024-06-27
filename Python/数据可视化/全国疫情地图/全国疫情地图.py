import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("数据可视化/全国疫情地图/疫情.txt", "r", encoding="UTF-8")
data = f.read()
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["today"]["confirm"]
    data_list.append((province_name, province_confirm))
map = Map()
map.add("各省份疫情确诊人数", data_list, "china")
map.set_global_opts(title_opts=TitleOpts(title="全国疫情确诊人数地图"),
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
map.render("全国疫情确诊人数地图.html")