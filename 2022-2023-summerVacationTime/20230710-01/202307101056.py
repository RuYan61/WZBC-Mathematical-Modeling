"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023-07-10 10:56
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Mathematical-Modeling
@File              : 202307101056.py
"""


import numpy as np
import pandas as pd

xlsxpath = "./CUMCM2022Problems E/附件.xlsx"

data = pd.read_excel(xlsxpath)
print(data)

data_numpy = np.array(data)