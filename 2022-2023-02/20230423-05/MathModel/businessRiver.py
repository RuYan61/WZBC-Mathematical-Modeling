
# 商人过河：
# 面向过程编程

# python无需声明变量类型
num = 3  # 商人与随从数量
boat_limit = 2  # 小船限制人数

# 1、创建 岸上 允许状态的列表S
S = []
for i in range(0, num + 1):
    if i == 0 or i == num:
        for j in range(0, num + 1):
            S.append((i, j))
    else:
        S.append((i, i))

# 2、创建 船上 允许决策的列表D
D = []
for u in range(0, boat_limit + 1):
    for v in range(0, boat_limit + 1):
        if 1 <= u + v <= boat_limit:
            D.append((u, v))

# 3、开始过河
start = (num, num)  # 此岸初始状态
end = (0, 0)  # 此岸最终状态
# L_x_y：船的位置与岸上的状态组成新的元祖 的列表（队列）：之所以
L_x_y = [(0, start)]

step_dict = {}
is_solution = 0  # 是否有解
while len(L_x_y) != 0:
    q_pop = L_x_y.pop(0)  # 删除L_x_y内第0个位置的元素，同时将获取被删除的元素q_pop：(0, start)
    if q_pop[0] == 0:  # 如果在此岸
        for x in D:  # 遍历 船上 允许决策列表[(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]
            temp_s = (q_pop[1][0] - x[0], q_pop[1][1] - x[1])
            if temp_s not in S:
                continue
            if (1, temp_s) in step_dict:
                continue
            L_x_y.append((1, temp_s))
            step_dict[(1, temp_s)] = q_pop
            if temp_s == end:
                is_solution = 1
                break
    else:
        for x in D:
            temp_s = (q_pop[1][0] + x[0], q_pop[1][1] + x[1])
            if temp_s not in S:
                continue
            if (0, temp_s) in step_dict:
                continue
            L_x_y.append((0, temp_s))
            step_dict[(0, temp_s)] = q_pop
    if is_solution == 1:
        break

if is_solution == 1:
    print('该问题有解！最短路径：')
    # 从后向前搜索
    path = [(1, end)]
    while path[-1] != (0, start):
        path.append(step_dict[path[-1]])
    path.reverse()
    # 美化输出
    real_path = list(map(str, path))
    for i in range(len(real_path)):
        if i != len(real_path) - 1:
            print(real_path[i] + '->')
        else:
            print(real_path[i])
else:
    print('该问题无解')
