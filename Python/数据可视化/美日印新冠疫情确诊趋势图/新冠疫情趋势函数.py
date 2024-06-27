import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, TooltipOpts


# 打开文件
def File_opening(s):
    text = open(s, "r", encoding="UTF-8")
    # text = open(s, "r", encoding="UTF-8")
    data = text.read()
    data = data.split("(", 1)[1]
    data = data[:-2]
    my_dict = json.loads(data)
    # trend_data = my_dict['data'][0]['trend']
    table = my_dict['data'][0]['name']
    # 获取日期数据
    X_date = my_dict['data'][0]['trend']['updateDate'][:314]
    # 获取确诊数据
    Y_data = my_dict['data'][0]['trend']['list'][0]['data'][:314]
    line = Line()
    line.add_xaxis(X_date)
    line.add_yaxis("确诊人数", Y_data)
    line.set_global_opts(
        title_opts=TitleOpts(pos_left="center", pos_bottom="1%"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(
            is_show=True,
            max_=20000000,
        ),
        tooltip_opts=TooltipOpts(is_show=True),
    )
    line.render(f"{table}.html")


if __name__ == "__main__":
    File_opening("数据可视化/美日印新冠疫情确诊趋势图/美国.txt")
