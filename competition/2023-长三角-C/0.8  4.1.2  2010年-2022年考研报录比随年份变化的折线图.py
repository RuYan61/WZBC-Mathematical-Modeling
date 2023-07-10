# 导入matplotlib库
import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 定义数据
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022] # 年份
y = [2.96, 3.06, 3.18, 3.25, 3.14, 2.89, 3, 2.78, 3.12, 3.57, 3.44, 3.59, 4.14] # 报录比（n:1，省略“:1”）

# 创建一个画布
plt.figure(dpi=600)

# 绘制折线图
plt.plot(x,y,label="报录比（n:1，省略“:1”）",marker="o",markersize=3,color="red")

# 设置x轴和y轴的标签
plt.xlabel("年份（年）")
plt.ylabel("报录比（n:1，省略“:1”）")

# 设置标题
plt.title("2010年-2022年考研报录比随年份变化的折线图")

# 设置图例
plt.legend()

# 显示图形
plt.show()
