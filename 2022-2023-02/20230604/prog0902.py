"""
Author: Wisdom Weng
Date:   2023/5/21
"""
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
from pprint import pprint
file_path = 'mooc/statistic_model/data/'


class FileOS:
    @staticmethod
    def load_txt_data(file_name, fields_name):
        data = []
        with open(os.path.join(file_path, file_name), 'r') as f:
            for i in f.readlines():
                data.append(i.replace('\n', '').split('\t'))
        data = pd.DataFrame(data, columns=fields_name)
        data.set_index('编号', inplace=True)
        data = data.astype(float)
        return data


class Model:
    @staticmethod
    def linear_regress_by_sklearn(x, y, alpha=0.05):
        lr = LinearRegression(fit_intercept=True)
        lr.fit(x, y)
        coef = np.r_[lr.intercept_, lr.coef_]
        # 残差-方差估计量
        residual = y - lr.predict(x)
        df = x.shape[0] - x.shape[1] - 1
        s_2 = residual.dot(residual)/df
        # 置信区间
        x0 = stats.t(df=df).ppf(alpha/2)
        X = np.c_[np.ones((x.shape[0], 1)), x]
        Skk = np.linalg.inv(np.dot(X.T, X)).diagonal()
        mse = np.sqrt(s_2 * Skk)
        left = coef + mse * x0
        right = coef + mse * (-x0)
        confidence_interval = np.c_[left, right]
        # 每个参数的p值
        tkk = coef / mse
        p_values = 2 * (1 - stats.t(df=df).cdf(np.abs(tkk)))
        # R方 / 调整后的R方
        r_square = 1 - s_2*df/sum((y-y.mean())**2)
        r_square_adj = 1 - ((1-r_square)*(x.shape[0]-1) / df)
        # F统计量
        f = (df / x.shape[1]) * (r_square / (1 - r_square))
        # 模型的p值
        p_value = 1 - stats.f(dfn=x.shape[1], dfd=df).cdf(f)

        coefficient_params = {'系数估计': coef, '置信区间': confidence_interval, 'P值': p_values, 't值': tkk, '标准误差': mse}
        model_params = {'R方': r_square, '调整后的R方': r_square_adj, '模型的p值': p_value, 'F统计量': f,
                        '方差估计': s_2, '残差平方和': s_2 * df}
        print("系数估计结果:")
        pprint(coefficient_params)
        print("模型估计结果:")
        pprint(model_params)
        model_params.update({'残差': residual})
        return coefficient_params, model_params

    @staticmethod
    def linear_regress_by_statsmodels(x, y):
        # 添加常数列
        x = sm.add_constant(x)
        model = sm.OLS(y, x)
        result = model.fit()
        pprint(result.summary())
        # coefficient_params = {'系数估计': result.params, '置信区间': result.conf_int(), 'P值': result.pvalues, 't值': result.tvalues, '标准误差': result.bse}
        # model_params = {'R方': result.rsquared, '调整后的R方': result.rsquared_adj, '模型的p值': result.f_pvalue, 'F统计量': result.fvalue,
        #                 '方差估计': result.scale, '残差平方和': result.ssr}
        # print("系数估计结果:")
        # pprint(coefficient_params)
        # print("模型估计结果:")
        # pprint(model_params)
        # model_params.update({'残差': result.resid})
        return result


class Prog0902(Model):
    def __init__(self):
        self.fields1 = ['资历', '管理', '教育']
        self.fields2 = ['教育-中学', '教育-大学', '组合类别']
        self.y_field = '薪金'
        self.data = FileOS.load_txt_data(file_name='data0902.txt',
                                         fields_name=['编号', self.y_field] + self.fields1 + self.fields2)

    def analysis(self):
        # 资历/管理/教育-无交互作用
        y = self.data[self.y_field].values
        x = self.data.loc[:, self.fields1[:-1] + self.fields2[:-1]].values
        coefficient_params, model_params = self.linear_regress_by_sklearn(x, y, alpha=0.05)
        result = self.linear_regress_by_statsmodels(x, y)

        # 增加交互项
        x1 = np.c_[x, x[:, 1]*x[:, 2], x[:, 1] * x[:, 3]]
        coefficient_params, model_params = self.linear_regress_by_sklearn(x1, y, alpha=0.05)
        result = self.linear_regress_by_statsmodels(x1, y)

        # 剔除异常点
        n = 33
        x2 = np.r_[x1[:n-1, :], x1[n:, :]]
        y2 = np.r_[y[:n-1], y[n:]]
        coefficient_params, model_params = self.linear_regress_by_sklearn(x2, y2, alpha=0.05)
        result = self.linear_regress_by_statsmodels(x2, y2)


class Prog0904(Model):
    def __init__(self):
        y = [90.9, 97.4, 113.5, 125.7, 122.8, 133.3, 149.3, 144.2, 166.4, 195.0, 229.8, 228.7, 206.1, 257.9, 324.1,
             386.6, 423.0, 401.9, 474.9, 424.5]
        x1 = [596.7, 637.7, 691.1, 756.0, 799.0, 873.4, 944.0, 992.7, 1077.6, 1185.9, 1326.4, 1434.2, 1549.2, 1718.0,
              1918.3, 2163.9, 2417.8, 2631.7, 2954.7, 3073.0]
        x2 = [0.7167, 0.7277, 0.7436, 0.7676, 0.7906, 0.8254, 0.8679, 0.9145, 0.9601, 1.0000, 1.0575, 1.1508, 1.2579,
              1.3234, 1.4005, 1.5042, 1.6342, 1.7842, 1.9514, 2.0688]
        self.data = pd.DataFrame([y, x1, x2]).T

    def analysis(self):
        y = self.data.iloc[:, 0].values
        x = self.data.iloc[:, 1:].values
        coefficient_params, model_params = self.linear_regress_by_sklearn(x, y, alpha=0.05)
        result = self.linear_regress_by_statsmodels(x, y)

        # 杜宾检验
        x = sm.add_constant(x)
        model = sm.OLS(y, x)
        result = model.fit()
        dw_statistic = sm.stats.durbin_watson(result.resid)



