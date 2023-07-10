# 导入matplotlib库
import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 定义数据
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022] # 年份
y = [33.75, 32.73, 31.49, 30.74, 31.90, 34.60, 33.33, 35.93, 32.02, 27.97, 29.04, 27.87, 24.15] # 录取率

# 创建一个画布
plt.figure(dpi=600)

# 绘制折线图
plt.plot(x,y,label="录取率（%）",marker="o",markersize=3,color="red")

# 设置x轴和y轴的标签
plt.xlabel("年份（年）")
plt.ylabel("录取率（%）")

# 设置标题
plt.title("2010年-2022年考研录取率随年份变化的折线图")

# 设置图例
plt.legend()

# 显示图形
plt.show()
