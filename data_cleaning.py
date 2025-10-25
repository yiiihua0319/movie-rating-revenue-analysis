import os
import pandas as pd

# 建立資料夾（如果沒有 data/ 就自動建立）
os.makedirs("data", exist_ok=True)

# 1️⃣ 讀入資料
df = pd.read_csv("movies.csv")

# 2️⃣ 確保數值欄位是正確型態
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
df['Metascore'] = pd.to_numeric(df['Metascore'], errors='coerce')
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

# 3️⃣ Genre 只取第一個分類
df['Genre'] = df['Genre'].astype(str).str.split(',').str[0].str.strip()

# 4️⃣ 建 decade 欄位（例如 1994 → 1990）
df['Decade'] = (df['Year'] // 10) * 10

# 5️⃣ 丟掉沒有 Score 或 Revenue 的列（畫散點圖需要）
df = df.dropna(subset=['Score', 'Revenue'])

# 6️⃣ 儲存乾淨版
df.to_csv("data/movies_clean.csv", index=False)

# 7️⃣ 用 IQR 法刪除極端值（outlier）
Q1 = df['Revenue'].quantile(0.25)
Q3 = df['Revenue'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR  # 可加這行讓下界也有定義，但票房不太可能太低所以通常用上界就好

df_iqr = df[(df['Revenue'] >= lower_bound) & (df['Revenue'] <= upper_bound)].copy()

# 8️⃣ 輸出「去除 outlier」版本
df_iqr.to_csv("data/movies_clean_no_outliers.csv", index=False)

# 9️⃣ 輸出摘要資訊
print("✅ Done.")
print(f"Original rows: {len(df)}")
print(f"After removing outliers: {len(df_iqr)}")
print(f"Upper bound (Q3 + 1.5*IQR): {upper_bound:.2f} M USD")
print("\n📊 Descriptive statistics (without outliers):")
print(df_iqr[['Score', 'Revenue']].describe())



