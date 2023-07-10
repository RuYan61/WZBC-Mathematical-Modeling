# pulp库求线性规划

# 导入包 import pulp
# 调用包中的类 和 调用对象中的函数 写法相同 都用.
# 代码来源 https://www.cnblogs.com/youcans/p/14714085.html


# from pulp import *
import pulp

# （1）定义一个规划问题
# 创建pulp.LpProblem的对象
# 参数 sense 用来指定求最小值/最大值问题，可选参数值：LpMinimize、LpMaximize 。
prob = pulp.LpProblem(name='汽车生产01', sense=pulp.LpMaximize)

# （2）定义决策变量
# 　pulp.LpVariable 是定义决策变量的函数。
# 　参数 lowBound、upBound 用来设定决策变量的下界、上界
# 　参数 cat 用来设定变量类型，可选参数值：
#           'Continuous' 表示连续变量（默认值）、
#           'Integer' 表示离散变量（用于整数规划问题）、
#           'Binary' 表示0/1变量（用于0/1规划问题）。

# 第 i 种货物装入第 j 个货舱的重量(吨)
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')

M = 10000
y1 = pulp.LpVariable('y1', cat='Binary')
y2 = pulp.LpVariable('y2', cat='Binary')
y3 = pulp.LpVariable('y3', cat='Binary')

# 3. 设置目标函数 z 利润
prob += 2 * x1 + 3 * x2 + 4 * x3

# 4. 施加约束
# 货仓重量
prob += (1.5 * x1 + 3 * x2 + 5 * x3 <= 600)
prob += (280 * x1 + 250 * x2 + 400 * x3 <= 60000)
prob += (280 * x1 + 250 * x2 + 400 * x3 <= 60000)

prob += (x1 <= M * y1)
prob += (x1 >= 80 * y1)
prob += (x2 <= M * y2)
prob += (x2 >= 80 * y2)
prob += (x3 <= M * y3)
prob += (x3 >= 80 * y3)

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
