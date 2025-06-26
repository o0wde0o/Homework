import pandas as pd

# 统计每个科目的成绩信息
file_path = "student_scores.xlsx"  # 文件路径
data = pd.read_excel(file_path, index_col="姓名") # 读取数据
# 分析数据并统计每个科目的成绩信息
data = data.drop("学号", axis=1 )  #删除学号列
stats = {}
for subject in data.columns:
    unique = sorted(data[subject].unique())  # 出现过的分数
    max = data[subject].max()  # 最高分
    min = data[subject].min()  # 最低分
    avg = data[subject].mean()  # 平均分
    stats[subject] = {
        "出现过的分数": unique,
        "最高分": max,
        "最低分": min,
        "平均分": avg,
    }


# 打印统计结果
for subject, stat in stats.items():
    print(f"{subject}: \n  出现过的分数: {stat['出现过的分数']}\n  最高分: {stat['最高分']}\n  最低分: {stat['最低分']}\n  平均分: {stat['平均分']:.2f}\n")
