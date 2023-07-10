import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 配置宋体文字
plt.rcParams['font.family'] = ['Songti SC']

# 定义分段函数
def f(x):
    return np.piecewise(x, [(1 <= x) & (x < 3), (3 <= x) & (x <= 5)], [lambda x: (1 + 1.1086*(x - 0.8942)**-2)**-1, lambda x: 0.3915*np.log(x) + 0.3699])

# 定义评级和得分的数据
x_labels = ['很差', '差', '一般', '好', '很好']
x_values = np.arange(1, 6)

# 生成横坐标的数值
x = np.linspace(1, 5, 100)

# 计算分段函数的函数值
y = f(x)

# 创建一个画布
plt.figure(dpi=600)

# 绘制图像
plt.plot(x, y, color='blue', linewidth=2)

# 设置纵坐标范围
plt.ylim(0, 1)

# 设置横坐标刻度为中文标签
plt.xticks(x_values, x_labels)

# 添加网格线
plt.grid(True)

# 添加标签和标题
plt.xlabel('')
plt.ylabel('')
plt.title('')

# 展示图像
plt.show()
