from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

f = open("E:/代码/Python/数据可视化/动态柱状图/1960-2019全球GDP数据.csv", "r", encoding="UTF-8")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条无用信息
data_lines.pop(0)
timeline = Timeline()
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(
            title=f"{year}年全球GDP前8数据"
        )
    )
    timeline.add(bar, str(year))
timeline.add_schema(
    play_interval=1000, is_timeline_show=True, is_auto_play=True, is_loop_play=False
)
timeline.render("1960年到2019年全球GDP前8国家.html")
