# 导入matplotlib库
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 配置宋体文字
plt.rcParams['font.family'] = ['Songti SC']

# 定义数据
x = [2017, 2018, 2019, 2020] # 年份
y = [43.78, 44.96, 48.23, 49.10] # 往届生占比

# 计算增长率列表
growth_rates = [((y[i] - y[i-1]) / y[i-1] * 100) for i in range(1,len(y))]

# 创建一个画布
plt.figure(dpi=600)

# 绘制折线图
plt.plot(x,y,label="往届生占比（%）",marker="o",markersize=3)
plt.plot(x[1:],growth_rates,label="往届生占比增长率（%）",marker="o",markersize=3)

# 设置x轴为整数
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# 设置x轴和y轴的标签
plt.xlabel("年份（年）")
plt.ylabel("往届生占比（%）和往届生占比增长率（%）")

# 设置标题
plt.title("2017年-2020年考研往届生占比和往届生占比增长率的折线图")

# 设置图例
plt.legend()

# 显示图形
plt.show()
