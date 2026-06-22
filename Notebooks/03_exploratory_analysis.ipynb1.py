import pandas as pd
import matplotlib.pyplot as plt

fund_master = pd.read_csv("../data/processed/fund_master_cleaned.csv")
nav_history = pd.read_csv("../data/processed/nav_history_cleaned.csv")
scheme_performance = pd.read_csv("../data/processed/scheme_performance_cleaned.csv")

print(fund_master.shape)
print(nav_history.shape)
print(scheme_performance.shape)

scheme_performance.describe()
risk_counts = fund_master['risk_category'].value_counts()
print(risk_counts)
top_funds = scheme_performance.sort_values(
    by='return_1yr_pct',
    ascending=False
).head(10)

print(top_funds[['scheme_name', 'return_1yr_pct']])
plt.figure(figsize=(10,5))

plt.bar(
    top_funds['scheme_name'],
    top_funds['return_1yr_pct']
)

plt.title("Top 10 Funds by 1-Year Return")
plt.xlabel("Scheme Name")
plt.ylabel("Return (%)")

plt.xticks(rotation=90)

plt.show()

avg_1yr = scheme_performance['return_1yr_pct'].mean()
avg_3yr = scheme_performance['return_3yr_pct'].mean()
avg_5yr = scheme_performance['return_5yr_pct'].mean()

print("Average 1-Year Return:", round(avg_1yr,2))
print("Average 3-Year Return:", round(avg_3yr,2))
print("Average 5-Year Return:", round(avg_5yr,2))

# Highest AUM Funds

top_aum = scheme_performance.sort_values(
    by='aum_crore',
    ascending=False
).head(5)

print("\nTop 5 Funds by AUM")
print(top_aum[['scheme_name', 'aum_crore']])
# Average Returns Analysis

avg_1yr = scheme_performance['return_1yr_pct'].mean()
avg_3yr = scheme_performance['return_3yr_pct'].mean()
avg_5yr = scheme_performance['return_5yr_pct'].mean()

print("Average 1-Year Return:", round(avg_1yr, 2))
print("Average 3-Year Return:", round(avg_3yr, 2))
print("Average 5-Year Return:", round(avg_5yr, 2))
top_aum = scheme_performance.sort_values(
    by='aum_crore',
    ascending=False
).head(10)

print(top_aum[['scheme_name', 'aum_crore']])
plt.figure(figsize=(14,6))

plt.bar(
    top_funds['scheme_name'],
    top_funds['return_1yr_pct']
)

plt.title("Top 10 Funds by 1-Year Return")
plt.xlabel("Scheme Name")
plt.ylabel("Return (%)")

plt.xticks(rotation=90)

plt.tight_layout()

plt.show()

# Average Returns Analysis

print("Average 1-Year Return:",
      round(scheme_performance['return_1yr_pct'].mean(),2))

print("Average 3-Year Return:",
      round(scheme_performance['return_3yr_pct'].mean(),2))

print("Average 5-Year Return:",
      round(scheme_performance['return_5yr_pct'].mean(),2))

print("\n===== Average Returns Analysis =====")

print("Average 1-Year Return:",
      round(scheme_performance['return_1yr_pct'].mean(), 2))

print("Average 3-Year Return:",
      round(scheme_performance['return_3yr_pct'].mean(), 2))

print("Average 5-Year Return:",
      round(scheme_performance['return_5yr_pct'].mean(), 2))

plt.show()

print("\n===== Average Returns Analysis =====")
print("Average 1-Year Return:", round(scheme_performance['return_1yr_pct'].mean(), 2))
print("Average 3-Year Return:", round(scheme_performance['return_3yr_pct'].mean(), 2))
print("Average 5-Year Return:", round(scheme_performance['return_5yr_pct'].mean(), 2))

input("\nPress Enter to exit...") 

plt.bar(top10["scheme_name"], top10["returns_1yr_pct"])
plt.xticks(rotation=90)
plt.tight_layout()