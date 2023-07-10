import numpy as np

columns = ['总占地面积', '寝室总人数', '卫浴间总面积', '盥洗室总面积', '大型服务面积', '小型服务面积', '电梯个数']
data = np.array([[877.4, 184, 55.1, 27.5, 0, 0, 0],
                 [2660, 220, 356.4, 55.4, 313.8, 93.2, 4],
                 [2229, 228, 344.0, 42.4, 0, 73.4, 5],
                 [1886.6, 132, 79.2, 95.0, 0, 0, 5]])

# 功效系数
data_gx = np.empty([data.shape[0], data.shape[1]])
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        data_gx[i, j] = 0.4 * (data[i, j] - np.min(data[:, j])) / (np.max(data[:, j]) - np.min(data[:, j])) + 0.6

# 熵值
data_ei = np.empty(data.shape[1])
for j in range(data.shape[1]):
    data_ei[j] = sum(data_gx[:, j] * np.log(data_gx[:, j])) / (-np.log(data.shape[0]))

# 权重
data_wj = (1 - data_ei) / sum((1 - data_ei))

# 计算方案评估值得分
eval_scores = np.sum(data_gx * data_wj, axis=1)

# 对评估值得分进行排序
sorted_indices = np.argsort(eval_scores)[::-1]  # 降序排列的索引

# 打印评估值得分和排序
print("方案评估值得分：", eval_scores)
print("方案排序：", sorted_indices)
