import pandas as pd
import matplotlib.pyplot as plt

fund_master = pd.read_csv("../data/raw/fund_master.csv")

print(fund_master.shape)
print(fund_master.head())
fund_master["risk_category"].value_counts().plot(kind="bar")
plt.title("Risk Category Distribution")
plt.show()

top10 = scheme_performance.sort_values(
    "return_1yr_pct",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.barh(top10["scheme_name"], top10["return_1yr_pct"])
plt.title("Top 10 Funds by 1-Year Return")
plt.tight_layout()
plt.show()
top_aum = scheme_performance.sort_values(
    "aum_crore",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.barh(top_aum["scheme_name"], top_aum["aum_crore"])
plt.title("Top 10 Funds by AUM")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8,5))
plt.scatter(
    scheme_performance.csv["return_1yr_pct"],
    scheme_performance.csv["sharpe_ratio"]
)

plt.xlabel("1-Year Return (%)")
plt.ylabel("Sharpe Ratio")
plt.title("Return vs Sharpe Ratio")
plt.show()
dashboard_data = pd.read_csv(
    "../data/dashboard/dashboard_data.csv"
)

print(dashboard_data.shape)
print(fund_master.columns.tolist())