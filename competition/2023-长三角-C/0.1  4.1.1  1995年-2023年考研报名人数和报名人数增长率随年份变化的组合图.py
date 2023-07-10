# 导入matplotlib库
import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.sans-serif'] = ['Songti SC']

# 定义年份和报名数列表
years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
enrollments = [15.50, 20.40, 24.20, 27.40, 31.90, 39.20, 46.00, 62.40, 79.70, 94.50, 117.20, 127.12, 128.20, 120.00, 124.60, 140.60, 151.10, 165.60, 176.00, 172.00, 164.90, 177.00, 201.00, 238.00, 290.00, 341.00, 377.00, 457.00, 474.00]

# 计算增长率列表
growth_rates = []
for i in range(1,len(enrollments)):
    growth_rate = (enrollments[i] - enrollments[i-1]) / enrollments[i-1] * 100
    growth_rates.append(growth_rate)

# 创建一个新的图形
plt.figure(dpi=600)

# 绘制年份和增长率的折线图，标签为"报名人数增长率（%）"
plt.plot(years[1:],growth_rates,label="报名人数增长率（%）",marker="o",markersize=3)

# 绘制年份和报名数的柱形图，标签为"报名人数（万）"，设置颜色为橙色
plt.bar(years,enrollments,label="报名人数（万）",color="orange")

# 设置x轴的标签为"年份（年）"
plt.xlabel("年份（年）")

# 设置y轴的标签为"报名人数和报名人数增长率"
plt.ylabel("报名人数和报名人数增长率")

# 设置标题为"1995年-2023年考研报名人数和报名人数增长率随年份变化的组合图"
plt.title("1995年-2023年考研报名人数和报名人数增长率随年份变化的组合图")

# 显示图例
plt.legend()

# 显示图形
plt.show()
