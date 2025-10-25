import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取資料
df = pd.read_csv("movies_clean.csv")

# 設定圖表風格
sns.set(style="whitegrid", font_scale=1.2)

# ---- Overall ----
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Score", y="Revenue", color="steelblue", s=80, alpha=0.8)
plt.title("Overall Relationship: Movie Score vs Revenue", fontsize=16, weight="bold")
plt.xlabel("IMDB Score")
plt.ylabel("Revenue (Million USD)")
plt.tight_layout()
plt.savefig("scatter_overall.png", dpi=300)
plt.show()

# ---- By Decade ----
g = sns.FacetGrid(df, col="Decade", col_wrap=3, height=4)
g.map_dataframe(sns.scatterplot, x="Score", y="Revenue", color="darkorange", alpha=0.8)
g.set_titles("Decade: {col_name}s")
g.set_axis_labels("IMDB Score", "Revenue (Million USD)")
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Score vs Revenue by Decade", fontsize=16, weight="bold")
plt.savefig("scatter_by_decade.png", dpi=300)
plt.show()

# ---- By Genre ----
g = sns.FacetGrid(df, col="Genre", col_wrap=4, height=4)
g.map_dataframe(sns.scatterplot, x="Score", y="Revenue", color="teal", alpha=0.8)
g.set_titles("{col_name}")
g.set_axis_labels("IMDB Score", "Revenue (Million USD)")
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Score vs Revenue by Genre", fontsize=16, weight="bold")
plt.savefig("scatter_by_genre.png", dpi=300)
plt.show()
