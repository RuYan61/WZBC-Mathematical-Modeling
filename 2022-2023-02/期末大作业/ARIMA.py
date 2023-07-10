import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


def run_arima_analysis():
    # 读取Excel文件中的数据
    df = pd.read_excel('附件.xlsx', parse_dates=['时间'])

    # 过滤数据，仅保留在指定时间范围内的数据
    start_date = pd.to_datetime('2010-01-01')
    end_date = pd.to_datetime('2023-03-01')
    df = df[(df['时间'] >= start_date) & (df['时间'] <= end_date)]

    # 设置时间列作为索引，并将其转换为每月一号的频率
    df = df.set_index('时间')
    df = df.resample('MS').mean()

    # 构建自回归积分滑动平均模型（ARIMA）
    model = sm.tsa.ARIMA(df['猪肉（去骨统肉）'], order=(1, 0, 1))

    # 训练模型并进行拟合
    model_fit = model.fit()

    # 预测未来的猪肉价格
    start_date = pd.to_datetime('2010-01-01')
    end_date = pd.to_datetime('2023-12-01')
    forecast = model_fit.predict(start=start_date, end=end_date)

    # 绘制原始数据和预测结果的图表
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['猪肉（去骨统肉）'], label='Actual')
    plt.plot(forecast.index, forecast, label='Forecast')
    plt.title('Predicted Pork Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 分析模型的结果和变化趋势
    print(model_fit.summary())


if __name__ == '__main__':
    run_arima_analysis()
