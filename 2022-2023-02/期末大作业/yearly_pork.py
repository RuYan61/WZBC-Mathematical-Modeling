import pandas as pd
import matplotlib.pyplot as plt


def plot_pork_prices(dataframe, time_column, pork_column):
    # 提取所需列数据
    data = dataframe[[time_column, pork_column]]

    # 将时间列设置为索引
    data.set_index(time_column, inplace=True)

    # 将时间列转换为日期时间类型
    data.index = pd.to_datetime(data.index)

    # 按年份对数据进行分组和月度重采样
    data_grouped = data.resample('M').sum()

    # 提取每年的数据
    years = data_grouped.index.year.unique()

    # 绘制每年的折线图
    for year in years:
        year_data = data_grouped[data_grouped.index.year == year]
        plt.plot(year_data.index.month, year_data[pork_column], label=str(year))

    # 设置图形标题和标签
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置宋体作为默认字体
    plt.title('年度猪肉（去骨统肉）集贸市场价格当期值')
    plt.xlabel('月份')
    plt.ylabel('猪肉（去骨统肉）集贸市场价格当期值(元/公斤)')
    plt.legend()

    # 显示图形
    plt.show()


# 主函数
def main():
    # 读取 Excel 文件
    df = pd.read_excel('附件.xlsx')

    # 定义时间列和猪肉列的名称
    time_column = '时间'
    pork_column = '猪肉（去骨统肉）'

    # 调用封装的函数进行绘图
    plot_pork_prices(df, time_column, pork_column)


# 调用主函数
if __name__ == '__main__':
    main()

