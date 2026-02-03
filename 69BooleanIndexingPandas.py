import pandas as pd

df = pd.read_csv('RandDatas/tips.csv')
lower_tips = df[df['tip'] < 4]
print(lower_tips)
