# 导入matplotlib库
import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 定义数据
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022] # 年份
y1 = [140.60, 151.10, 165.60, 176.00, 172.00, 164.90, 177.00, 201.00, 238.00, 290.00, 341.00, 377.00, 457.00] # 报名人数（万）
y2 = [47.44, 49.46, 52.13, 54.09, 54.87, 57.06, 58.98, 72.22, 76.25, 81.13, 99.05, 105.07,110.35] # 录取人数（万）

# 创建一个画布
plt.figure(dpi=600)

# 绘制柱形图
plt.bar(x,y1,label="报名人数（万）")
plt.bar(x,y2,label="录取人数（万）")

# 设置x轴和y轴的标签
plt.xlabel("年份（年）")
plt.ylabel("报名人数（万）和录取人数（万）")

# 设置标题
plt.title("2010年-2022年考研报名人数和录取人数随年份变化的柱形图")

# 设置图例
plt.legend()

# 显示图形
plt.show()
