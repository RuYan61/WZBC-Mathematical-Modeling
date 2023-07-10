import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.family'] = ['Songti SC']

# 定义横坐标和纵坐标的标签
x_labels = ['0', '很不满意', '不太满意', '较满意', '满意', '很满意']
y_labels = [0, 0.2, 0.4, 0.6, 0.8, 1]
x_values = list(range(len(x_labels)))  # 横坐标从 0 开始递增

# 创建一个画布
plt.figure(dpi=600)

# 绘制图形
plt.plot(x_labels, y_labels, marker='o')

# 获取当前坐标轴对象
ax = plt.gca()

# 将左边框和底部边框设置为原点所在的位置
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# 将右边框和顶部边框隐藏
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# 添加网格线
plt.grid(True)

# 设置图形标题和坐标轴标签
plt.title('')
plt.xlabel('')
plt.ylabel('')

# 显示图形
plt.show()


