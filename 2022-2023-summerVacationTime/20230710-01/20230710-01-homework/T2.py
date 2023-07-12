"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023-07-12 13:20
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Mathematical-Modeling
@File              : T2.py
"""


import pandas as pd


def statistics_by_wuliao():
    df = pd.read_excel("附件.xlsx")

    wuliao_counts = df["物料编码"].value_counts().sort_values(ascending=False)

    selected_materials = wuliao_counts.index[:6].tolist()
    filtered_df = df[df["物料编码"].isin(selected_materials)]

    grouped_df = filtered_df.groupby("物料编码").agg({
        "需求量": ["max", "mean", "median", "var"],
        "销售单价": ["max", "mean", "var"],
    }).reset_index()

    grouped_df.columns = ["物料编码", "需求最大值", "需求平均数", "需求中位数", "需求方差", "单价最大值", "单价平均值", "单价方差"]

    grouped_df = grouped_df.applymap(lambda x: round(x, 2) if isinstance(x, (int, float)) else x)
    grouped_df = grouped_df.transpose()

    print(grouped_df)
    grouped_df.to_excel("T2-统计选定物料的数据.xlsx")


def main():
    statistics_by_wuliao()


if __name__ == "__main__":
    main()
