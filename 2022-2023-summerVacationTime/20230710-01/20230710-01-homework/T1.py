"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023-07-12 13:09
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Mathematical-Modeling
@File              : T1.py
"""


import pandas as pd


def count_by_wuliao():
    df = pd.read_excel("附件.xlsx")

    wuliao_counts = df["物料编码"].value_counts().sort_index().reset_index()

    wuliao_counts.columns = ["物料编码", "数量"]

    print(wuliao_counts)
    wuliao_counts.to_excel("T1-统计所有物料的编号以及出现的次数.xlsx")


def main():
    count_by_wuliao()


if __name__ == "__main__":
    main()
