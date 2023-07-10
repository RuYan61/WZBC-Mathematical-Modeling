# pulp库求线性规划

# 导入包 import pulp
# 调用包中的类 和 调用对象中的函数 写法相同 都用.
# 代码来源 https://www.cnblogs.com/youcans/p/14714085.html


# from pulp import *
import pulp

# （1）定义一个规划问题
# 创建pulp.LpProblem的对象
# 参数 sense 用来指定求最小值/最大值问题，可选参数值：LpMinimize、LpMaximize 。
prob = pulp.LpProblem(name='自来水输送', sense=pulp.LpMinimize)

# （2）定义决策变量
# 　pulp.LpVariable 是定义决策变量的函数。
# 　参数 lowBound、upBound 用来设定决策变量的下界、上界
# 　参数 cat 用来设定变量类型，可选参数值：
#           'Continuous' 表示连续变量（默认值）、
#           'Integer' 表示离散变量（用于整数规划问题）、
#           'Binary' 表示0/1变量（用于0/1规划问题）。

# 水库i  向j 区的日供水量为 xij
x11 = pulp.LpVariable('x11', lowBound=0, cat='Continuous')
x12 = pulp.LpVariable('x12', lowBound=0, cat='Continuous')
x13 = pulp.LpVariable('x13', lowBound=0, cat='Continuous')
x14 = pulp.LpVariable('x14', lowBound=0, cat='Continuous')
x21 = pulp.LpVariable('x21', lowBound=0, cat='Continuous')
x22 = pulp.LpVariable('x22', lowBound=0, cat='Continuous')
x23 = pulp.LpVariable('x23', lowBound=0, cat='Continuous')
x24 = pulp.LpVariable('x24', lowBound=0, cat='Continuous')
x31 = pulp.LpVariable('x31', lowBound=0, cat='Continuous')
x32 = pulp.LpVariable('x32', lowBound=0, cat='Continuous')
x33 = pulp.LpVariable('x33', lowBound=0, cat='Continuous')
x34 = pulp.LpVariable('x34', lowBound=0, cat='Continuous')

# 3. 设置目标函数 z
prob += 160 * x11 + 130 * x12 + 220 * x13 + 170 * x14 + \
        140 * x21 + 130 * x22 + 190 * x23 + 150 * x24 + \
        190 * x31 + 200 * x32 + 230 * x33

# 4. 施加约束
# 供应限制
prob += (x11 + x12 + x13 + x14 == 50)
prob += (x21 + x22 + x23 + x24 == 60)
prob += (x31 + x32 + x33 == 50)
# 需求限制
# 注意不能写成(30 =< x11 + x21 + x31 <= 80) 虽然不报错但系统自动忽略左侧
prob += (x11 + x21 + x31 <= 80)
prob += (x11 + x21 + x31 >= 30)
prob += (x12 + x22 + x32 <= 140)
prob += (x12 + x22 + x32 >= 70)
prob += (x13 + x23 + x33 <= 30)
prob += (x13 + x23 + x33 >= 10)
prob += (x14 + x24 <= 50)
prob += (x14 + x24 >= 10)

# 5. 求解
# solve() 是求解函数。PuLP默认采用 CBC 求解器来求解优化问题，
# 也可以调用其它的优化器来求解，如：GLPK，COIN CLP/CBC，CPLEX，和GUROBI，但需要另外安装。　
prob.solve()
print(prob.name)
print("Status:", pulp.LpStatus[prob.status])  # 输出求解状态
for v in prob.variables():
    print(v.name, "=", v.varValue)  # 输出每个变量的最优值
print("F(x) = ", pulp.value(prob.objective))  # 输出最优解的目标函数值

# # 6. 打印求解状态
# print("Status:", pulp.LpStatus[prob.status])
#
# # 8. 打印最优解的目标函数值
# print("z= ", pulp.value(prob.objective))
#
# # 7. 打印出每个变量的最优值
# for v in prob.variables():
#     print(v.name, "=", v.varValue)
