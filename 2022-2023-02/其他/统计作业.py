import os
import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'D:/BaiduSyncdisk/温导论文/收作业/温导人名单.xlsx')

# 创建一个空集合来存储已提交作业的学生学号
submitted_students = set()

# 遍历文件夹中的文件
folder_path = 'D:/BaiduSyncdisk/温导论文/收作业/通过'  # 替换为你的作业文件夹路径
for folder_name in os.listdir(folder_path):
    # 提取文件夹名称的前几位作为学号，并转换为字符串类型
    student_id = str(folder_name[7:18])
    # 将已提交作业的学生学号加入集合
    submitted_students.add(student_id)

# 统计未提交作业的学生
missing_students = []
for index, row in df.iterrows():
    student_id = str(row['学号'])  # 将学号转换为字符串类型
    student_name = row['姓名']
    if student_id not in submitted_students:
        missing_students.append((student_id, student_name))

# 打印未提交作业的学生学号和姓名
print("未提交作业的学生:")
for student_id, student_name in missing_students:
    print(f"学号: {student_id}, 姓名: {student_name}")
