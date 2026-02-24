import pandas as pd
import numpy as np

data = {
    "study_hours":    [2, 4, 6, 8, 10, 3, 7, 5, 9, 1],
    "sleep_hours":    [9, 7, 6, 5, 4,  8, 5, 6, 4, 10],
    "exam_score":     [45, 60, 72, 85, 95, 50, 80, 68, 91, 30],
    "phone_usage_hrs":[6, 5, 4, 3, 1,  6, 2, 4, 2, 7],
}

df = pd.DataFrame(data)

corr_matrix = df.corr()

print("=== Correlation Matrix ===")
print(corr_matrix.round(2))
