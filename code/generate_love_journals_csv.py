import os
import re
import pandas as pd

# 设置目录和文件前缀
folder = "final_project/generated_journals"
file_prefix = "journal_run_"
file_count = 5

data = []

# 遍历 5 个文件
for i in range(1, file_count + 1):
    filepath = os.path.join(folder, f"{file_prefix}{i}.txt")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 匹配所有 [Day X] 内容块
    entries = re.findall(r"\[Day (\d+)\](.*?)(?=\[Day \d+\]|\Z)", content, re.DOTALL)
    
    for day_str, text in entries:
        data.append({
            "version": i,
            "day": int(day_str),
            "text": text.strip().replace("\n", " ")
        })

# 保存为 CSV
df = pd.DataFrame(data)
df.sort_values(by=["version", "day"], inplace=True)
df.to_csv("final_project/love_journals_dataset.csv", index=False, encoding="utf-8")

print("✅ Saved as final_project/love_journals_dataset.csv")
