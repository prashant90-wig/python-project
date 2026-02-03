import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42) # Make random numbers predictable

# Features (X): Study Hours
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Labels (y): Test Scores with some noise
# Pattern: score = 10 * hours + 30 + noise
test_scores = 10 * study_hours + 30 + np.random.randn(10) * 5

print("Study Hours:", study_hours)
print("Test Scores:", test_scores)

# Visualize the data
plt.scatter(study_hours, test_scores)
plt.xlabel('Study Hours')
plt.ylabel('Test Score')
plt.title('Study Hours vs Test Scores')
plt.show()




