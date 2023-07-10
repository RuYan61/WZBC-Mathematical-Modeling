import matplotlib.pyplot as plt

# 数据
labels = ['A', 'B', 'C', 'D', 'E']
values = [80.83, 74.73, 90.13, 79.67, 37.46]

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置宋体作为默认字体

# 创建一个画布
plt.figure(dpi=600)

# 创建柱状图
plt.bar(labels, values, color='skyblue', edgecolor='gray')

# 添加数据标签
for i, value in enumerate(values):
    plt.text(i, value, f'{value}%', ha='center', va='bottom')

# 设置标题和标签
plt.title('14.您认为民营经济发展面临的主要挑战是？[多选题]', fontsize=16)
plt.xlabel('选项字母', fontsize=12)
plt.ylabel('每个选项中选择该选项的比例 (%)', fontsize=12)

# 调整坐标轴刻度字体大小
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 调整坐标轴标签旋转角度
plt.xticks(rotation=45)

# 添加网格线
plt.grid(axis='y', linestyle='--')

# 移除上边框和右边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 显示图形
plt.show()
