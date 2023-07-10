"""
允许状态集合，例num=3
S={(x,y)|x=0,y=0,1,2,3;x=3,y=0,1,2,3;x=y=1,2} x是此岸的商人数，y是此岸的仆人数
允许决策集合，例boat_limit=2
D={(u,v)|1<=u+v<=2,u,v=0,1,2} u是撘载的商人数，v是搭载的仆人数
"""

num = eval(input("共有商仆对数："))
boat_limit = eval(input("船容量："))
temp = []

for i in range(0, num+1, 1):
    if i == 0 or i == num:
        for j in range(0, num+1, 1):
            temp.append((i, j))
    else:
        temp.append((i, i))

S = set(temp)
D = []

for u in range(0, boat_limit+1):
    for v in range(0, boat_limit+1):
        if u+v >= 1 and u+v <= boat_limit :
            D.append((u,v))

start = (num,num)
end = (0,0)
queue = []
queue.append((0, start))    # 前面的元素如果是0，说明是船在此岸，是1，说明船在对岸
step_dict = {}
flag = 0
finish = []

while len(queue) != 0:
    q_pop = queue.pop(0)
    if q_pop[0] == 0:
        for x in D:
            temp_s = (q_pop[1][0] - x[0], q_pop[1][1] - x[1])
            if temp_s not in S:
                continue
            if (1, temp_s) in step_dict:
                continue
            queue.append((1, temp_s))
            step_dict[(1, temp_s)] = q_pop
            if temp_s == end:
                flag = 1
                finish = (1, temp_s)
                break
    else:
        for x in D:
            temp_s = (q_pop[1][0] + x[0], q_pop[1][1] + x[1])
            if temp_s not in S:
                continue
            if (0, temp_s) in step_dict:
                continue
            queue.append((0, temp_s))
            step_dict[(0, temp_s)] = q_pop
    if flag == 1:
        break

steps = int(-1)

if flag == 1:
    print("该问题有解！输出格式为（1为船在彼岸时/0为船在此案时， （商人数， 随从数））最短路径：")
    path = []
    path.append(finish)
    while path[-1] != (0, start):
        path.append(step_dict[path[-1]])
    path.reverse()
    real_path = list(map(str, path))
    for i in range(len(real_path)):
        if i != len(real_path)-1:
            steps += 1
            if steps == 0:
                print("开始时：", end="")
                print(real_path[i] + "->")
            else:
                print("第" + str(steps) + "步：", end="")
                print(real_path[i] + "->")
        else:
            steps += 1
            print("第" + str(steps) + "步：", end="")
            print(real_path[i])
            print("最少需要" + str(steps) + "步")
else:
    print("该问题无解")
