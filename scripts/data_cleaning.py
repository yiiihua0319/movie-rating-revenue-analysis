import pandas as pd
df = pd.read_csv("movies.csv")
df = df.replace("NA", pd.NA)
rows_with_na = df.isna().any(axis=1).sum()
print("Rows with at least one null value:", rows_with_na)
df_clean = df.dropna()
df_1418 = df_clean[(df_clean["Year"] >= 2014) & (df_clean["Year"] <= 2018)].copy()
df_1418["Revenue"] = pd.to_numeric(df_1418["Revenue"], errors="coerce")
cpi_factor = {
   2014: 1.060705,  # 251.107 / 236.736
   2015: 1.059447,  # 251.107 / 237.017
   2016: 1.046249,  # 251.107 / 240.007
   2017: 1.024425,  # 251.107 / 245.120
   2018: 1.0        # 251.107 / 251.107
}
df_1418["cpi_factor"] = df_1418["Year"].map(cpi_factor)
df_1418["real_revenue_2018"] = df_1418["Revenue"] * df_1418["cpi_factor"]
target_genres = ["Drama", "Comedy", "Action", "Adventure"]
genre_dummies_all = df_1418["Genre"].str.get_dummies(sep=", ")
available_genres = [g for g in target_genres if g in genre_dummies_all.columns]
genre_dummies = genre_dummies_all[available_genres]
mask_has_target = genre_dummies.sum(axis=1) > 0
df_1418_4 = df_1418.loc[mask_has_target].copy()
for g in available_genres:
   df_1418_4[g] = genre_dummies.loc[mask_has_target, g]
print("Counts of each target genre (2014–2018):")
print(df_1418_4[available_genres].sum())x
output_file = "movies_clean_2014_2018_4genres_inflation_adj.csv"
df_1418_4.to_csv(output_file, index=False)
print("Cleaned file saved to:", output_file)
