"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023-07-12 13:51
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Mathematical-Modeling
@File              : T3.py
"""


import pandas as pd
import matplotlib.pyplot as plt


def read_excel_and_screen_df():
    df = pd.read_excel("附件.xlsx")
    wuliao_counts = df["物料编码"].value_counts().sort_values(ascending=False)
    selected_materials = wuliao_counts.index[:6].tolist()
    filtered_df = df[df["物料编码"].isin(selected_materials)]
    return selected_materials, filtered_df


def scatter(selected_materials, filtered_df, title, xlabel, ylabel, xticks, yticks):
    plt.figure(dpi=600, figsize=(10, 8))
    colors = plt.cm.tab10.colors[:len(selected_materials)]

    for i, material in enumerate(selected_materials):
        material_data = filtered_df[filtered_df["物料编码"] == material]
        plt.scatter(material_data[xticks], material_data[yticks], label=material, color=colors[i])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.title(title)
    plt.legend()
    plt.show()

    for material in selected_materials:
        plt.figure(dpi=600, figsize=(10, 8))
        material_data = filtered_df[filtered_df["物料编码"] == material]
        plt.scatter(material_data[xticks], material_data[yticks], label=material, color=colors[selected_materials.index(material)])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.title("物料" + str(material) + "的" + title)
        plt.legend()
        plt.show()


def plot(selected_materials, filtered_df, title, xlabel, ylabel, xticks, yticks):
    plt.figure(dpi=600, figsize=(10, 8))
    colors = plt.cm.tab10.colors[:len(selected_materials)]

    for i, material in enumerate(selected_materials):
        material_data = filtered_df[filtered_df["物料编码"] == material]
        plt.plot(material_data[xticks], material_data[yticks], label=material, color=colors[i])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.title(title)
    plt.legend()
    plt.show()

    for material in selected_materials:
        plt.figure(dpi=600, figsize=(10, 8))
        material_data = filtered_df[filtered_df["物料编码"] == material]
        plt.plot(material_data[xticks], material_data[yticks], label=material, color=colors[selected_materials.index(material)])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.title("物料" + str(material) + "的" + title)
        plt.legend()
        plt.show()


def main():
    selected_materials, filtered_df = read_excel_and_screen_df()
    plt.rcParams['font.sans-serif'] = ['Songti SC']
    scatter(selected_materials, filtered_df, "需求与价格之间的散点图", "销售单价", "需求量", "销售单价", "需求量")
    scatter(selected_materials, filtered_df, "需求与时间之间的散点图", "日期", "需求量", "日期", "需求量")
    plot(selected_materials, filtered_df, "需求与价格之间的折线图", "销售单价", "需求量", "销售单价", "需求量")
    plot(selected_materials, filtered_df, "需求与时间之间的折线图", "日期", "需求量", "日期", "需求量")


if __name__ == "__main__":
    main()
