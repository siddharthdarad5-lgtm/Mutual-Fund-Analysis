import pandas as pd

df = pd.read_csv("fund_master.csv")
print(df.head)
print(df['fund_house'].value_counts())
print(df['category'].value_counts())
print(df['sub_category'].value_counts())
