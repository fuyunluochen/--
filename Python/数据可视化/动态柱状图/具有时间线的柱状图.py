from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [20, 25, 15], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [25, 30, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

# 创建时间线对象
timeline = Timeline()
# timeline对象添加Bar柱状图
timeline.add(bar1, "2010年GDP")
timeline.add(bar2, "2020年GDP")
# 自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
# 通过时间线绘图
timeline.render("带时间线的柱状图.html")
