# 导入matplotlib库
import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.family'] = ['Songti SC']

# 准备数据
x1 = [49.10, 50.90]
x2 = [48.23, 51.77]
x3 = [44.96, 55.04]
x4 = [43.78, 56.22]

# 准备标签
labels = ['往届生占比', '应届生占比']

# 创建一个画布，并设置大小和清晰度
plt.figure(dpi=600)

# 设置整个画布的标题
plt.suptitle("2017年-2020年考研往届生占比和应届生占比的饼图")

# 第一张饼图
plt.subplot(2, 2, 4)
plt.pie(x1, labels=labels, autopct='%1.2f%%')

# 设置子标题
plt.title("2020年")

# 第二张饼图
plt.subplot(2, 2, 3)
plt.pie(x2, labels=labels, autopct='%1.2f%%')

# 设置子标题
plt.title("2019年")

# 第三张饼图
plt.subplot(2, 2, 2)
plt.pie(x3, labels=labels, autopct='%1.2f%%')

# 设置子标题
plt.title("2018年")

# 第四张饼图
plt.subplot(2, 2, 1)
plt.pie(x4, labels=labels, autopct='%1.2f%%')

# 设置子标题
plt.title("2017年")

# 调整子图间距
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# 显示图形
plt.show()
