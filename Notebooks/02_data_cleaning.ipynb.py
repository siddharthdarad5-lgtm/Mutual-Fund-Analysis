import pandas as pd
import numpy as np

fund_master = pd.read_csv("../data/raw/fund_master.csv")
nav_history = pd.read_csv("../data/raw/nav_history.csv")
scheme_performance = pd.read_csv("../data/raw/scheme_performance.csv")

print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)
print("Scheme Performance Shape:", scheme_performance.shape)
fund_master.head()
fund_master.isnull().sum()
nav_history.isnull().sum()
scheme_performance.isnull().sum()
print("Fund Master Duplicates:", fund_master.duplicated().sum())
print("NAV History Duplicates:", nav_history.duplicated().sum())
print("Scheme Performance Duplicates:", scheme_performance.duplicated().sum())
fund_codes = set(fund_master['amfi_code'])
nav_codes = set(nav_history['amfi_code'])

print("Fund Master Codes:", len(fund_codes))
print("NAV Codes:", len(nav_codes))
print("Missing Codes:", len(nav_codes - fund_codes))

import os

os.makedirs("../data/processed", exist_ok=True)

fund_master.to_csv("../data/processed/fund_master_cleaned.csv", index=False)
nav_history.to_csv("../data/processed/nav_history_cleaned.csv", index=False)
scheme_performance.to_csv("../data/processed/scheme_performance_cleaned.csv", index=False)

print("Cleaned files saved successfully!")


