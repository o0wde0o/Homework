import random
import numpy as np
import pandas as pd

# 学生姓名元组
student_names = (
    "李明哲", "张婉如", "王梓轩", "刘思琪", "陈嘉伟", "杨梦瑶",
    "赵天宇", "黄欣怡", "周俊杰", "吴雨萱", "徐浩然", "孙雅婷",
    "胡志强", "朱梓萱", "高雨欣", "郭子豪", "曹文轩", "许慧敏",
    "韩雪婷", "冯子轩", "程思远", "谢佳欣", "唐紫轩", "沈浩然",
    "曾梦琪", "雷蕾", "汪梓涵", "陆子轩", "蒋欣怡", "蔡嘉伟",
    "余婉如", "魏天宇", "叶梓萱", "邹雨欣", "熊子豪", "白嘉怡",
    "蒋浩然", "邱婉婷", "黎子轩", "陶思琪", "薛嘉伟", "殷梦瑶",
    "樊天宇", "尹梓轩", "段欣怡", "章俊杰", "汪雨萱", "范思远",
    "韦紫轩", "金雅婷"
)

# 随机选择20个不重复学生名字
selected_students = random.sample(student_names, 20)

# 科目名称
subjects = ["语文", "数学", "英语", "物理", "化学", "生物", "地理"]

# 生成成绩数据（正态分布，四舍五入取整数）
# 语数英：均值105，标准差15，范围[0, 120]
subject_150 = np.clip(np.random.normal(105, 15, (20, 3)), 0, 120).round()

# 物化生地：均值85，标准差15，范围[0, 100]
subject_100 = np.clip(np.random.normal(85, 15, (20, 4)), 0, 100).round()

# 合并所有科目成绩
scores = np.hstack((subject_150, subject_100))

# 创建学号
student_ids = [f"{i:02}" for i in range(1, 21)]  # 生成01到20的学号

# 创建DataFrame
df = pd.DataFrame(scores, columns=subjects, index=selected_students)
df.insert(0, "学号", student_ids)  # 将学号插入为第一列

# 导出为Excel文件
file_path = "student_scores.xlsx"
df.to_excel(file_path, index_label="姓名")

print(f"学生成绩表已保存到: {file_path}")
