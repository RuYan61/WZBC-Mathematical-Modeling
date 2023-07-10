import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def calculate_correlations(filename):
    # 读取Excel文件
    data = pd.read_excel(filename)

    # 提取所需的列数据
    column_names = data.columns
    pork_prices = data[column_names[-1]]  # 猪肉价格列

    # 转换时间列为数值型数据
    time_column = data[column_names[0]]
    time_values = pd.to_numeric(time_column, errors='coerce')

    # 创建空列表存储相关系数和列名
    correlations = []

    # 计算最后一列与前面每一列的相关系数
    for i in range(1, len(column_names) - 1):
        column_name = column_names[i]
        column_data = data[column_name]

        # 处理时间列的数据类型
        if pd.api.types.is_datetime64_any_dtype(column_data):
            column_data = pd.to_numeric(column_data, errors='coerce')

        correlation, _ = pearsonr(pork_prices, column_data)
        correlations.append((column_name, correlation))

    # 计算时间列与猪肉价格的皮尔逊相关系数
    time_corr, _ = pearsonr(time_values, pork_prices)
    correlations.append(("时间", time_corr))

    # 根据相关系数降序排序
    correlations.sort(key=lambda x: x[1], reverse=True)

    return correlations


def plot_correlations(correlations):
    # 提取列名和相关系数
    labels = [x[0] for x in correlations]
    coefficients = [x[1] for x in correlations]

    # 输出相关系数数据
    for column, correlation in correlations:
        print(f"猪肉价格与{column} 的皮尔逊积矩相关系数：{format(correlation, '.20f')}")

    # 输出相关系数数据并添加到柱形图上
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置宋体作为默认字体
    plt.figure(dpi=600)
    plt.bar(labels, coefficients)
    plt.xticks(rotation=90)
    plt.xlabel("各因素（除时间：集贸市场价格当期值(元/公斤)）")
    plt.ylabel("相关系数")
    plt.title("猪肉价格与各因素的皮尔逊积矩相关系数")

    # 添加柱形上的数据标签
    for i in range(len(labels)):
        plt.text(i, coefficients[i], format(coefficients[i], '.3f'), ha='center', va='bottom')

    # 添加水平虚线
    for i in range(1, int(max(coefficients) * 10) + 2):
        plt.axhline(i * 0.1, color='orange', linestyle='--', zorder=0)

    plt.tight_layout()
    plt.show()


def main():
    filename = '附件.xlsx'
    correlations = calculate_correlations(filename)
    plot_correlations(correlations)


if __name__ == "__main__":
    main()
