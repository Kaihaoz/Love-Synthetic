import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Load CSV
df = pd.read_csv("final_project/love_journals_dataset.csv")

# Compute sentiment polarity for each entry
def compute_sentiment(text):
    return TextBlob(text).sentiment.polarity

df["sentiment"] = df["text"].apply(compute_sentiment)

# Convert types for safety
df["version"] = df["version"].astype(int)
df["day"] = df["day"].astype(int)

# Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="day", y="sentiment", hue="version", marker="o", palette="tab10")

plt.title("Sentiment Trend Over 10 Days in AI Love Journals")
plt.xlabel("Day")
plt.ylabel("Sentiment Score (Polarity)")
plt.ylim(-1, 1)
plt.legend(title="Journal Version", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Save figure
plt.savefig("final_project/sentiment_trend.png", dpi=300)
plt.show()
