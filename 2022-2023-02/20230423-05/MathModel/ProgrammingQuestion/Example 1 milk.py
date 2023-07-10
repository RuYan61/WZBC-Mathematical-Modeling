
# pulp库求线性规划

# 导入包 import pulp
# 调用包中的类 和 调用对象中的函数 写法相同 都用.
# 代码来源 https://www.cnblogs.com/youcans/p/14714085.html


# from pulp import *
import pulp

# （1）定义一个规划问题
# 创建pulp.LpProblem的对象
# 参数 sense 用来指定求最小值/最大值问题，可选参数值：LpMinimize、LpMaximize 。
prob = pulp.LpProblem(name='奶制品加工', sense=pulp.LpMaximize)

# （2）定义决策变量
# 　pulp.LpVariable 是定义决策变量的函数。
# 　参数 lowBound、upBound 用来设定决策变量的下界、上界
# 　参数 cat 用来设定变量类型，可选参数值：
#           'Continuous' 表示连续变量（默认值）、
#           'Integer' 表示离散变量（用于整数规划问题）、
#           'Binary' 表示0/1变量（用于0/1规划问题）。
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')

# 3. 设置目标函数 z
# 对象 += 目标函数式 (+=可以想象成往milkMake对象里面拼接式子)
prob += 72*x1 + 64*x2

# 4. 施加约束
# 对象 += 约束条件表达式
prob += (x1 + x2 <= 50)  # 不等式约束
prob += (12*x1 + 8*x2 <= 480)
prob += (3*x1 <= 100)

# 5. 求解
# solve() 是求解函数。PuLP默认采用 CBC 求解器来求解优化问题，
# 也可以调用其它的优化器来求解，如：GLPK，COIN CLP/CBC，CPLEX，和GUROBI，但需要另外安装。　
prob.solve()
print(prob.name)
print("求解状态:", pulp.LpStatus[prob.status])  # 输出求解状态
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

