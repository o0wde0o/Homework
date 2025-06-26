import pandas as pd

# 读取数据
file_path = "student_scores.xlsx"  # 文件路径
data = pd.read_excel(file_path, index_col="姓名")

# 提取学号
student_ids = data["学号"]
data = data.drop(columns=["学号"])  # 防止学号被误算为成绩

# 定义科目权重
subject_150 = ["语文", "数学", "英语"]  # 权重 150 分的科目
subject_100 = ["物理", "化学", "生物", "地理"]  # 权重 100 分的科目

# 初始化总成绩和加权平均分
data["总成绩"] = 0
data["加权平均分"] = 0

for subject in subject_150:
    data["总成绩"] += data[subject]
    data["加权平均分"] +=data[subject]/1.5 # 150 分权重科目换算成百分制
for subject in subject_100:
    data["总成绩"] += data[subject]
    data["加权平均分"] +=data[subject] # 100 分权重科目无需换算

# 计算加权平均分（保留两位小数）
data["加权平均分"] = (data["加权平均分"]/ 7).round(2)

# 计算每科排名
for subject in subject_150 + subject_100:
    data[f"{subject}排名"] = data[subject].rank(ascending=False, method="min")

# 重排列顺序：每科成绩后紧跟排名
columns_order = []
for subject in subject_150 + subject_100:
    columns_order.extend([subject, f"{subject}排名"])
columns_order.extend(["总成绩", "加权平均分"])  # 将总成绩和加权平均分放在末尾
data = data[columns_order]

# 按总成绩降序排序
data = data.sort_values(by="总成绩", ascending=False)

# 将学号插入回表格第一列
data.insert(0, "学号", student_ids)

# 打印第一名的数据
print("第一名的数据如下：")
print(data.iloc[0])

# 导出结果
rank_file = "student_ranks.xlsx"  # 排名文件路径
data.to_excel(rank_file, index_label="姓名")  # 导出排名数据

print(f"排名数据已保存到: {rank_file}")
