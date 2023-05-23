from pyecharts.charts import Bar
from pyecharts.faker import Faker
import streamlit_echarts
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Line
from pyecharts.charts import Pie
import streamlit as st

if st.sidebar.checkbox("柱状图", True):
    bar = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint")
                            ,yaxis_opts=opts.AxisOpts(name="Y 轴")
                            ,xaxis_opts=opts.AxisOpts(name="X 轴"),)
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False), # 是否显示标签
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ]
            ),
        )
    )
    streamlit_echarts.st_pyecharts(bar)

if st.sidebar.checkbox("折线图", False):
    line = (
            Line()
            .add_xaxis(Faker.choose())
            .add_yaxis(
                "商家A",
                Faker.values(),
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
            .add_yaxis(
                "商家B",
                Faker.values(),
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkLine"))
        )
    streamlit_echarts.st_pyecharts(line)

if st.sidebar.checkbox("饼图", False):
    pie = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "75%"], # 饼图的半径，数组的第一项是内半径，第二项是外半径 # 默认设置成百分比，相对于容器高宽中较小的一项的一半
        )
        # .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-Radius"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%"  #orient 图例列表的布局朝向。可选：'horizontal', 'vertical'
            ),# pos_left 图例组件离容器左侧的距离。left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
            # 也可以是 'left', 'center', 'right'。# 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    streamlit_echarts.st_pyecharts(pie)

from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType

words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
]
if st.sidebar.checkbox("词云图", False):
    word = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape='circle')  # shape 词云图轮廓，有 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star' 可选
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-基本示例"))
    )
    streamlit_echarts.st_pyecharts(word)

import datetime
if st.sidebar.checkbox("地图", False):
    A=['武汉市', '孝感市', '黄冈市', '荆州市','鄂州市', '随州市', '襄阳市', '黄石市', '宜昌市', '荆门市', '咸宁市', '十堰市', '仙桃市','天门市',
    '恩施土家族苗族自治州', '潜江市','神农架林区']
    B=[47071,3482,2904,1576,1385,1305,1175,1008, 926, 920, 836,671,575,495,251,195,11]
    map_chart = Map()
    map_chart.add(
        "湖北",  # map name
        [list(z) for z in zip(A,B)],
        "湖北",
        is_map_symbol_show=False
    )

    map_chart.set_global_opts(
        title_opts=opts.TitleOpts(
            title="湖北确诊人数分布(" + str(datetime.date.today()) + ")"
        ),
        visualmap_opts=opts.VisualMapOpts(
            max_=10000,
            is_piecewise=True,
            pieces=[
                {"min": 1, "max": 99, "label": "100人以下", "color": "#FFE6BE"},
                {"min": 100, "max": 499, "label": "100-499人", "color": "#FFB769"},
                {"min": 500, "max": 1000, "label": "500-1000人", "color": "#FF8F66"},
                {"min": 1000, "max": 3000, "label": "1000-3000人", "color": "#ED514E"},
                {"min": 3000, "max": 100000, "label": "2000人以上", "color": "#CA0D11"}
            ]))
    streamlit_echarts.st_pyecharts(map_chart)
