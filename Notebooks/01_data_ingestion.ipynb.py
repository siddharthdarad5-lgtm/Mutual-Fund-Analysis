
import pandas as pd
import numpy as np

fund_master = pd.read_csv("../data/raw/fund_master.csv")
nav_history = pd.read_csv("../data/raw/nav_history.csv")
aum_by_fund_house = pd.read_csv("../data/raw/aum_by_fund_house.csv")
monthly_sip_inflows = pd.read_csv("../data/raw/monthly_sip_inflows.csv")
category_inflows = pd.read_csv("../data/raw/category_inflows.csv")
industry_folio_count = pd.read_csv("../data/raw/industry_folio_count.csv")
scheme_performance = pd.read_csv("../data/raw/scheme_performance.csv")
investor_transactions = pd.read_csv("../data/raw/investor_transactions.csv")
portfolio_holdings = pd.read_csv("../data/raw/portfolio_holdings.csv")
benchmark_indices = pd.read_csv("../data/raw/benchmark_indices.csv")

print("Fund Master:", fund_master.shape)
print("NAV History:", nav_history.shape)
print("scheme Performance:", scheme_performance.shape)
fund_master.dtypes
nav_history.dtypes
fund_master.head()
nav_history.head()
fund_master.isnull().sum()
nav_history.isnull().sum()
fund_master.duplicated().sum()
nav_history.duplicated().sum()
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("Fund Master Codes:", len(master_codes))
print("NAV Codes:", len(nav_codes))
print("Missing Codes:", len(master_codes - nav_codes))


