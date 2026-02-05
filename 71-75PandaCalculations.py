import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame({
    'name': ['Nana', 'Boruto', 'Kageyama', 'Hinata', 'Yuuichi'],
    'department': ['Sales', 'IT', 'Sales', 'IT', 'Sales'],
    'income': [50000, 60000, 55000, 70000, 52000],
    'age': [25, np.nan, 35, 28, np.nan]
})

# 71. Add new column
df['tax'] = df['income'] * 0.10
df['senior'] = df['age'] > 30

# 72. Drop missing values
df_clean = df.dropna()  # drops rows with ANY null
df_clean2 = df.dropna(subset=['age'])  # drops rows where age is null

# 73. Fill missing data
df['age_filled'] = df['age'].fillna(df['age'].mean())
df['age_filled2'] = df['age'].fillna(30)  # constant

# 74. Group by
avg_by_dept = df.groupby('department')['income'].mean()
summary = df.groupby('department').agg({
    'income': ['mean', 'sum', 'count'],
    'age': 'mean'
})

# 75. Pivot table
pivot = df.pivot_table(
    values='income',
    index='department',
    aggfunc='mean'
)

print(df)
print("\nAverage income by department:")
print(avg_by_dept)
print("\nPivot:")
print(pivot)