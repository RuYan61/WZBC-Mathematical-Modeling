# python 基本规则
# 1、强制缩进
# 2、创建变量时无须声明变量类型（nice）

a = 123
# aa = int(123)
b = 'abc'

# 1、函数调用规则：函数名(入参1，入参2，...)
# 不认识的函数可以百度查他的入参以及输出结果，或者查文档
# https://docs.python.org/zh-cn/3/
# 函数怎么来的？：
# （1）自己定义
# （2）python内置函数（print、abs），
# （3）调用对象方法
print('helloworld')
range(0, 10)

# 2.1、列表: []表示   属于：引用数据类型
c = [1, 3, 5, 7]
cc = list([1, 2, 3])
# 常用操作(内置方法)
# （1）列表取值
ele = c[0]
# （2）列表拼接 append()，可拼接任何数据类型
c.append(1)
# （3）删除列表中的元素 pop(index)
c.pop(0)

# 2.2、元祖：（）表示   属于：基本数据类型  python中与int str同类
d = (1, 2)
# 将元祖接入列表c
c.append(d)
# 元祖取值
d[0]

# 2.3、字典：{}
dict1 = {}
# 添加字典元素：键值对
dict1['a'] = 1

# 3、if判断：
aa = 123
bb = 'abc'
# or或  and与
# ==判断是否相等  !=判断是否不等
if aa == 123 or bb == 123:
    print('helloworld')
else:
    print('bye')

# 4.1、for循环：
# for 变量 in 结构体：包括列表、数组、元祖、字典、集合等等
# （强制缩进） 主体语句
# 例1：
# range(begin,end)可创建一个整数列表(begin ~ end-1)
for i in range(0, 10):
    print(i)  # 强制缩进

# 例2：嵌套循环
for i in range(0, 10):
    for j in range(5, 15):
        print(i, j)  # 强制缩进

# 练习1：如何通过 嵌套循环 拼接出列表 [(0, 0), (0, 1), (1, 0), (1, 1)]？

# 4.2、while循环
# while 条件
n = 10
while n != 0:
    n = n - 1
    print(n)
