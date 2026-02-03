import pandas as pd

df = pd.read_csv('RandDatas/tips.csv')

sorted_df = df.sort_values('total_bill')
print(sorted_df)

sorted_df_desc = df.sort_values('total_bill', ascending=False)
print(sorted_df_desc)