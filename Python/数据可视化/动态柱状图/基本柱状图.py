from pyecharts.charts import Bar
from pyecharts.options import *

# 构建柱状图对象
bar = Bar()
# 添加X轴数据
bar.add_xaxis(["中国", "美国", "俄罗斯"])
# 添加Y轴数据
bar.add_yaxis("GDP", [20, 27, 15], label_opts=LabelOpts(position="right"))
# 反转XY轴
bar.reversal_axis()
# 绘图
bar.render("基本柱状图.html")
