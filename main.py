import os
import pyecharts.options as opts
from pyecharts.charts import Line

print('请将此脚本放到R15根目录中')
cmd0 = os.getcwd() + r'\"CINEBENCH Windows 64 Bit".exe -cb_cpux >pyR15.txt'
cmd = os.getcwd() + r'\"CINEBENCH Windows 64 Bit".exe -cb_cpux >>pyR15.txt'

choice = input('输入y开始循环，输入n读取文件')
if choice == 'y':
    times = input('请输入R15循环的次数 \n')
    os.system(cmd0)
    for i in range(int(times) - 1):
        os.system(cmd)
        print('已经完成第', i + 1, '次')
else:
    print('请将txt文本文档改名为pyR15 将会自动生成')
    k = input('输入任意值开始生成')

print('正在生成曲线图')
with open('pyR15.txt', 'r') as f:
    lines = f.readlines()
    data = [x for i, x in enumerate(lines) if x.find('Rendering (Multiple CPU)') != -1]
nums = len(data)
for i in range(nums):
    data[i] = float(data[i][27:-5])
    data[i] = int(data[i])
    print('第', i + 1, '次得分：', end='')
    print(data[i])

x = range(nums)
y = data

line = (Line(init_opts=opts.InitOpts(bg_color="#9AC0CD"))
    .set_global_opts(
    tooltip_opts=opts.TooltipOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(type_="value", name='循环次数', ),
    yaxis_opts=opts.AxisOpts(
        type_="value",
        max_='2500',
        name='得分'),
)
    .add_xaxis(xaxis_data=x)
    .add_yaxis(
    linestyle_opts=opts.LineStyleOpts(width=5),
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值"), ]),
    markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_="average", name="平均值"),
              ]),
    series_name="R15循环跑分成绩",
    y_axis=y,
)
)

line.render('R15曲线图.html')
os.startfile('R15曲线图.html')
