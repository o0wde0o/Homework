import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# 设置字体支持中文
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
file_path = "student_ranks.xlsx"  # 文件路径
data = pd.read_excel(file_path, index_col="姓名")

# 提取学号后保留成绩数据
data = data.drop(columns=["学号"])

# 及格标准
pass_scores = {
    "语文": 90, "数学": 90, "英语": 90,
    "物理": 60, "化学": 60, "生物": 60, "地理": 60,
    "总成绩": 600, "加权平均分" : 60
}


# 计算及格率
def calculate_pass_rate():
    """计算所有科目及格率并绘制九宫格饼状图"""
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))  # 创建3x3的子图
    axes = axes.flatten()  # 展平成一维数组，便于索引
    total_students = len(data)

    for i, (subject, pass_score) in enumerate(pass_scores.items()):
        pass_count = (data[subject] >= pass_score).sum()
        fail_count = total_students - pass_count
        pass_rate = pass_count / total_students

        # 绘制饼状图
        axes[i].pie(
            [pass_count, fail_count],
            labels=["及格", "不及格"],
            autopct="%.2f%%",
            colors=["cyan", (0.5, 0.5, 0.5)],
            startangle=140
        )
        axes[i].set_title(f"{subject}\n及格率：{pass_rate:.2%}")

    plt.tight_layout()
    plt.show()


# 综合全部箱型图

def plot_boxplot_analysis():
    """绘制所有科目的箱型图"""
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))  # 创建3x3的子图
    axes = axes.flatten()  # 展平成一维数组，便于索引

    for i, (subject, _) in enumerate(pass_scores.items()):
        sns.boxplot(y=data[subject], color="skyblue", ax=axes[i])
        axes[i].set_title(f"{subject} 学生成绩箱形图")
        axes[i].set_ylabel("分数")

    # 隐藏多余的子图
    for j in range(len(pass_scores), len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    plt.show()

# 综合绘制某科目全部图形
def plot_subject_analysis(subject):
    """绘制某科目的所有图形：饼状图、箱形图、直方图"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))  # 创建1x3的子图

    # 调用各个绘图函数，并传入对应的子图对象
    plot_pass_pie(subject, axes[0])
    plot_boxplot(subject, axes[1])
    plot_histogram_with_pdf(subject, axes[2])

    # 调整子图间的间距并显示图形
    plt.tight_layout()
    plt.show()


# 绘制单科目饼状图
def plot_pass_pie(subject, ax):
    """绘制饼状图"""
    pass_count = (data[subject] >= pass_scores[subject]).sum()
    fail_count = len(data) - pass_count
    ax.pie(
        [pass_count, fail_count],
        labels=["及格", "不及格"],
        autopct="%.2f%%",
        colors=["cyan", (0.5, 0.5, 0.5)],
        startangle=140
    )
    ax.set_title(f"{subject} 及格比例")


# 绘制单科目箱形图
def plot_boxplot(subject, ax):
    """绘制箱形图"""
    sns.boxplot(y=data[subject], color="skyblue", ax=ax)
    ax.set_title(f"{subject} 学生成绩箱形图")
    ax.set_ylabel("分数")


# 绘制单科目直方图/分数分布及概率密度曲线
def plot_histogram_with_pdf(subject, ax):
    """绘制直方图及拟合概率密度曲线"""
    scores = data[subject]
    sns.histplot(scores, kde=False, bins=10, color="skyblue", stat="density", label="频率", ax=ax)
    mu, sigma = norm.fit(scores)
    x = np.linspace(scores.min(), scores.max(), 100)
    pdf = norm.pdf(x, mu, sigma)
    ax.plot(x, pdf, 'b-', label=f"拟合PDF (μ={mu:.2f}, σ={sigma:.2f})")
    ax.set_title(f"{subject} 分数分布及概率密度曲线")
    ax.set_xlabel("分数")
    ax.set_ylabel("密度")
    ax.legend()
    ax.grid()


# 主程序入口
def main():
    print("功能菜单：")
    print("1. 计算所有科目及格率并绘制饼状图")
    print("2. 绘制每一科目学生分数箱形图")
    print("3. 输入科目名称，绘制该科目的全部图形")
    choice = input("请选择功能编号 (1/2/3): ")

    if choice == "1":
        calculate_pass_rate()
    elif choice == "2":
        plot_boxplot_analysis()
    elif choice == "3":
        subject = input("请输入科目名称：")
        plot_subject_analysis(subject)
    else:
        print("无效选项，请重新运行程序！")

# 运行主程序
main()
