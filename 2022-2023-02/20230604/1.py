import pandas as pd

# 读取txt文件并转化为DataFrame
data = pd.read_csv('data0902.txt', delimiter='\t', header=None)
df = pd.DataFrame(data)

# 添加列名
df.columns = ['序号', '薪资', '就业年限', '管理责任', '教育程度']

# 将"教育程度"变量转化为虚拟变量
dummy_education = pd.get_dummies(df['教育程度'], prefix='教育程度')

# 将虚拟变量添加到原DataFrame中
df = pd.concat([df, dummy_education], axis=1)

# 对定量变量进行描述性统计
quantitative_variables = ['薪资', '就业年限', '管理责任']
quantitative_stats = df[quantitative_variables].describe()

# 对定性变量进行数量和比例统计
categorical_variables = ['教育程度']
categorical_counts = df[categorical_variables].value_counts()
categorical_proportions = df[categorical_variables].value_counts(normalize=True)

from sklearn.linear_model import LinearRegression

# 创建特征矩阵X和目标变量y
X = df[['就业年限', '管理责任', '教育程度_1', '教育程度_2', '教育程度_3']]
y = df['薪资']

# 创建线性回归模型并拟合数据
model = LinearRegression()
model.fit(X, y)

from sklearn.metrics import mean_squared_error

# 对训练数据进行预测
y_pred = model.predict(X)

# 计算均方误差（Mean Squared Error, MSE）
mse = mean_squared_error(y, y_pred)

import matplotlib.pyplot as plt

# 配置宋体文字
plt.rcParams['font.family'] = ['Songti SC']

# 创建一个画布
plt.figure(dpi=600)

# 绘制实际值与预测值的散点图
plt.scatter(y, y_pred)
plt.xlabel('实际值')
plt.ylabel('预测值')
plt.title('实际值与预测值的散点图')
plt.show()
