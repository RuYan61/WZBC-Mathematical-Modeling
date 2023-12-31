# 导入matplotlib库
import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 定义数据
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022] # 年份
y1 = [47.44, 49.46, 52.13, 54.09, 54.87, 57.06, 58.98, 72.22, 76.25, 81.13, 99.05, 105.07,110.35] # 录取人数（万）
y2 = [None, 4.25, 5.40, 3.75, -2.27, -4.13, 7.34, 13.56, 18.41, 21.85, 17.59, 6.08, 5.03] # 录取人数增长率

# 创建一个画布
plt.figure(dpi=600)

# 绘制折线图
plt.plot(x,y2,label="录取人数增长率（%）",marker="o",markersize=3)

# 绘制柱形图
plt.bar(x,y1,label="录取人数（万）",color="orange")

# 设置x轴和y轴的标签
plt.xlabel("年份（年）")
plt.ylabel("录取人数（万）和录取人数增长率（%）")

# 设置标题
plt.title("2010年-2022年考研录取人数增长率及其相关数据（录取人数）随年份变化的组合图")

# 设置图例
plt.legend()

# 显示图形
plt.show()
