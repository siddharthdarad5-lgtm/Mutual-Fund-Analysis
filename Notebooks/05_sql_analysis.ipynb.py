import pandas as pd
import sqlite3
fund_master = pd.read_csv("../data/raw/fund_master.csv")
print(fund_master.shape)
fund_master.head()
conn = sqlite3.connect("mutual_fund.db")
fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

query = """
SELECT COUNT(*) as total_funds
FROM fund_master
"""

result = pd.read_sql(query, conn)
print(result)

query = """
SELECT
    risk_category,
    COUNT(*) as fund_count
FROM fund_master
GROUP BY risk_category
"""

risk_summary = pd.read_sql(query, conn)

print(risk_summary)
query = """
SELECT
    category,
    COUNT(*) as fund_count
FROM fund_master
GROUP BY category
ORDER BY fund_count DESC
"""

category_summary = pd.read_sql(query, conn)

print(category_summary)
query = """
SELECT
    fund_house,
    COUNT(*) as total_funds
FROM fund_master
GROUP BY fund_house
ORDER BY total_funds DESC
"""

fund_house_summary = pd.read_sql(query, conn)

print(fund_house_summary)

import matplotlib.pyplot as plt

risk_summary.plot(
    x="risk_category",
    y="fund_count",
    kind="bar",
    legend=False
)

plt.title("Funds by Risk Category")
plt.show()