import pandas as pd

data = {
    "transaction_amount": [100, 150, 200, 250, 300, 350, 500000, 400, 450, 500],
}

df = pd.DataFrame(data)

def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower ) | (df[column] > upper)]
    clean = df[(df[column] >= lower) & (df[column] <= upper)]

    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Bounds: [{lower:.2f}, {upper:.2f}]")
    print(f"\n Outliers: \n{outliers}")
    print(f"\n Clean Data: \n{clean}")

    return clean, outliers

clean_df, outlier_df = detect_outliers_iqr(df, "transaction_amount")