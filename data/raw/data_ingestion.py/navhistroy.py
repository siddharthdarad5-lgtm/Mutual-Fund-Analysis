#import pandas as pd

 #nav = pd.read_csv("nav_history.csv") 

 # print(nav.head()) 
 # print(nav.shape)
 # print(nav.dtypes)
 # print(nav.shape)

 # print(nav.isnull().sum())

 # print(nav.duplicated().sum())

 # print(nav.columns)
 # nav['date'] = pd.to_datetime(nav['date'])
 #print(nav.dtypes)   
# COMPARING fund_master.csv aur nav_history.csv
import pandas as pd

fund_master = pd.read_csv("fund_master.csv")
nav = pd.read_csv("nav_history.csv")

master_codes = set(fund_master['amfi_code'])
nav_codes = set(nav['amfi_code'])

missing_codes = master_codes - nav_codes

print("Missing AMFI Codes:", missing_codes)
print("Count:", len(missing_codes))