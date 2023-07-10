import numpy as np

columns = ['人均总面积', '人均居住面积', '人均卫浴面积', '人均活动空间', '每个寝室人数', '长廊宽度', '长廊最大深度']
data = np.array([[4.77, 3.19, 0.30, 3.64, 8, 2.2, 12.4],
                 [12.09, 6.25, 1.62, 9.97, 4, 1.8, 21.6],
                 [9.78, 4.48, 1.51, 6.5, 6, 2.4, 42.9],
                 [14.29, 5.45, 0.6, 6.77, 2, 2.4, 55.8]])

# 同趋势化：4 6
data_re = data.copy()
data_re[:, 4] = 1 / data[:, 4]
data_re[:, 6] = 1 / data[:, 6]

# 归一
data_01 = np.empty([data_re.shape[0], data_re.shape[1]])
for j in range(data_re.shape[1]):
    for i in range(data_re.shape[0]):
        data_01[i, j] = data_re[i, j] / np.sqrt(sum(data_re[:, j] ** 2))

# 加权规范矩阵
w = [0.1060, 0.1177, 0.1785, 0.1183, 0.1822, 0.1751, 0.1222]
data_w = w * data_01

# 正负理想解
pis = np.max(data_w, axis=0)
nis = np.min(data_w, axis=0)

# 距离
pis_list = []
nis_list = []
for i in range(len(data_w)):
    pis_list.append(np.sqrt(sum((pis - data_w[i, :]) ** 2)))
    nis_list.append(np.sqrt(sum((nis - data_w[i, :]) ** 2)))

pis_arr = np.array(pis_list)
nis_arr = np.array(nis_list)

# 综合排序指标


# 计算 TOPSIS 得分
topsis_scores = nis_arr / (nis_arr + pis_arr)
print(topsis_scores)

# 对得分进行排序
sorted_indices = np.argsort(topsis_scores)[::-1]  # 降序排列的索引

# 根据排序结果重新排列数据矩阵
sorted_data = data[sorted_indices]

# 打印排序结果
print("排序结果：")
for i, index in enumerate(sorted_indices):
    print(f"排名第 {i+1} 的备选方案：", sorted_data[i])
