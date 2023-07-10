# A，B两个临时料场的坐标（单位：km）
A = (5, 1)
B = (2, 7)

# 六个建筑工地的坐标（单位：km）
JZ = [(1.25, 1.25), (8.75, 0.75), (0.5, 4.75), (5.75, 5), (3, 6.5), (7.25, 7.25)]

# A，B两个临时料场的水泥日储量
SNA = 20
SNB = 20

# 六个建筑工地的水泥日用量
SNJZ = [3, 5, 4, 7, 6, 11]

# A临时用料场到六个建筑工地的直线距离
JLA = [((A[0] - JZ[i][0]) ** 2 + (A[1] - JZ[i][1]) ** 2) ** 0.5 for i in range(6)]
# print(JLA)

# B临时用料场到六个建筑工地的直线距离
JLB = [((B[0] - JZ[i][0]) ** 2 + (B[1] - JZ[i][1]) ** 2) ** 0.5 for i in range(6)]
# print(JLB)

# 判断六个建筑工地分别离哪个建筑工地最近以及他们的差值
JLCZ = [JLA[i] - JLB[i] for i in range(6)]
# print(JLCZ)

# 从六个建筑工地中挑选两个水泥厂差值最大的先进行运输，并计算累计距离，注意约束条件
JLCZ_abs = [abs(JLCZ[i]) for i in range(6)]
# print(JLCZ_abs)
JLCZ_abs_sort = JLCZ_abs.copy()
JLCZ_abs_sort.sort()
# print(JLCZ_abs_sort)

i = 0
step = 1
Smin = 0

while i < 6:
    j = JLCZ_abs.index(JLCZ_abs_sort[-1 - i])

    if JLCZ[j] > 0 and SNB >= SNJZ[j]:
        SNB -= SNJZ[j]
        Smin += JLCZ_abs[j]
        print("第" + str(step) + "步：\nB临时料场往" + str(j + 1) + "号建筑工地运输" + str(SNJZ[j]) + "吨水泥，\n" + "B临时料场还剩" + str(SNB) +"吨水泥，\n" + "累计" + str("%.3f" % Smin) + "千米。\n")
        SNJZ[j] = 0
    elif JLCZ[j] > 0 and SNB < SNJZ[j]:
        Smin += JLCZ_abs[j]
        print("第" + str(step) + "步：\nB临时料场往" + str(j + 1) + "号建筑工地运输" + str(SNB) + "吨水泥，\n" + "B临时料场还剩0吨水泥，\n" + "累计" + str("%.3f" % Smin) + "千米。\n")
        SNJZ[j] -= SNB
        SNB = 0
        JLCZ[j] *= -1
        i -= 1
    elif JLCZ[j] < 0 and SNA >= SNJZ[j]:
        SNA -= SNJZ[j]
        Smin += JLCZ_abs[j]
        print("第" + str(step) + "步：\nA临时料场往" + str(j + 1) + "号建筑工地运输" + str(SNJZ[j]) + "吨水泥，\n" + "A临时料场还剩" + str(SNA) + "吨水泥，\n" + "累计" + str("%.3f" % Smin) + "千米。\n")
        SNJZ[j] = 0
    elif JLCZ[j] < 0 and SNA < SNJZ[j]:
        Smin += JLCZ_abs[j]
        print("第" + str(step) + "步：\nA临时料场往" + str(j + 1) + "号建筑工地运输" + str(SNA) + "吨水泥，\n" + "A临时料场还剩0吨水泥，\n" + "累计" + str("%.3f" % Smin) + "千米。\n")
        SNJZ[j] -= SNA
        SNA = 0
        JLCZ[j] *= -1
        i -= 1

    i += 1
    step += 1

js = 0

for i in range(6):
    if SNJZ[i] == 0:
        js += 1

if js == 6 and SNA >= 0 and SNB >= 0:
    print("以上步骤的总距离最短切成立。")
else:
    print("以上步骤不成立")