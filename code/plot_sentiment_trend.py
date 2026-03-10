import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 载入数据
df = pd.read_csv("final_project/love_journals_dataset.csv")

# 自我表达关键词
self_keywords = ["i", "me", "my", "myself", "mine", "am", "feel", "think"]

# 计算 selfhood score
def compute_selfhood(text):
    words = text.lower().split()
    if not words:
        return 0
    return sum(1 for w in words if w in self_keywords) / len(words)

# 应用到每段文本
df["selfhood_score"] = df["text"].apply(compute_selfhood)

# 类型转换
df["version"] = df["version"].astype(int)
df["day"] = df["day"].astype(int)

# 绘图：每日平均自我表达趋势
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="day", y="selfhood_score", hue="version", marker="o", palette="tab10")

plt.title("Selfhood Expression Trend Over 10 Days")
plt.xlabel("Day")
plt.ylabel("Selfhood Score (Proportion of Self-Referential Words)")
plt.ylim(-0.1, 0.3)
plt.legend(title="Journal Version", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# 保存图像
plt.savefig("final_project/selfhood_trend.png", dpi=300)
plt.show()
