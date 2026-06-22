import pandas as pd
import os

fund_master = pd.read_csv("../data/processed/fund_master_cleaned.csv")
nav_history = pd.read_csv("../data/processed/nav_history_cleaned.csv")
scheme_performance = pd.read_csv("../data/processed/scheme_performance_cleaned.csv")

print("Fund Master:", fund_master.shape)
print("NAV History:", nav_history.shape)
print("Scheme Performance:", scheme_performance.shape)
print(fund_master.columns.tolist())
print(scheme_performance.columns.tolist())
print(fund_master.columns.tolist())
print(scheme_performance.columns.tolist())

print(fund_master["risk_category"].value_counts())

top_funds = scheme_performance.sort_values(
    "return_1yr_pct",
    ascending=False
)

print(
    top_funds[
        ["scheme_name", "return_1yr_pct"]
    ].head(10)
)

merged_df = pd.merge(
    fund_master,
    scheme_performance,
    on="amfi_code",
    how="inner"
)

print(merged_df.shape)
avg_return = merged_df.groupby(
    "risk_category"
)["return_1yr_pct"].mean()

print(avg_return.sort_values(ascending=False))
print(
    scheme_performance[
        ["scheme_name", "sharpe_ratio"]
    ]
    .sort_values("sharpe_ratio", ascending=False)
    .head(10)
)
print(
    scheme_performance[
        ["scheme_name", "aum_crore"]
    ]
    .sort_values("aum_crore", ascending=False)
    .head(10)
)
print(
    fund_master["expense_ratio_pct"].describe()
)
print(
    scheme_performance[
        [
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "sharpe_ratio",
            "expense_ratio_pct"
        ]
    ].corr()
)

# Merge datasets
dashboard_data = pd.merge(
    fund_master,
    scheme_performance,
    on="amfi_code",
    how="inner"
)

# Dashboard folder create if not exists
os.makedirs("../data/dashboard", exist_ok=True)

# Export dashboard dataset
dashboard_data.to_csv(
    "../data/dashboard/dashboard_data.csv",
    index=False
)
dashboard_check = pd.read_csv("../data/dashboard/dashboard_data.csv")

print(dashboard_check.shape)
print(dashboard_check.head())

