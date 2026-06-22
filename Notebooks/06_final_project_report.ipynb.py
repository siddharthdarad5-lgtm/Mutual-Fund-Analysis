import pandas as pd

fund_master = pd.read_csv("../data/raw/fund_master.csv")
nav_history = pd.read_csv("../data/raw/nav_history.csv")
scheme_performance = pd.read_csv("../data/raw/scheme_performance.csv")

print("Files Loaded Successfully")
print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)
print("Scheme Performance Shape:", scheme_performance.shape)

print("\nFund Master Columns:")
print(fund_master.columns.tolist())

print("\nScheme Performance Columns:")
print(scheme_performance.columns.tolist())
print("\n===== DATASET SUMMARY =====")

print("Total Funds:", len(fund_master))
print("Total NAV Records:", len(nav_history))

print("\nRisk Distribution")
print(fund_master["risk_category"].value_counts())

print("\nCategory Distribution")
print(fund_master["category"].value_counts())
print("\n" + "="*60)
print("TOP 10 PERFORMING FUNDS (1 YEAR RETURN)")
print("="*60)

top_funds = scheme_performance.sort_values(
    by="return_1yr_pct",
    ascending=False
)

print(
    top_funds[
        ["scheme_name", "fund_house", "return_1yr_pct"]
    ].head(10)
)
print("\n" + "="*60)
print("RISK METRICS SUMMARY")
print("="*60)

risk_metrics = scheme_performance[
    [
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct"
    ]
].describe()

print(risk_metrics)

print("\n" + "="*60)
print("AVERAGE RETURNS BY CATEGORY")
print("="*60)

avg_return = scheme_performance.groupby(
    "category"
)["return_1yr_pct"].mean()

print(avg_return)

print("\n" + "="*60)
print("TOP 5 FUNDS BY AUM")
print("="*60)

top_aum = scheme_performance.sort_values(
    by="aum_crore",
    ascending=False
)

print(
    top_aum[
        ["scheme_name", "aum_crore"]
    ].head(5)
)