import numpy as np
import pandas as pd    # 导入pandas库，用于数据处理和分析
from sklearn.linear_model import LinearRegression

df = pd.read_excel("../附件_副本.xlsx")  # 使用pandas库读取Excel文件内容并创建DataFrame

md=LinearRegression().fit(df[:,:11],df[:,11])    #构建并拟合模型
y=md.predict(df[:,:11])       #求预测值
b0=md.intercept_; b12=md.coef_   #输出回归系数
R2=md.score(df[:,:11],df[:,11])      #计算R^2
print("b0=%.4f\nb12=%.4f%10.4f"%(b0,b12[0],b12[1]))
print("拟合优度R^2=%.4f"%R2)