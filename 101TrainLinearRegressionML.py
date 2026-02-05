import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create synthetic data
np.random.seed(42)
study_hours = np.arange(1, 11)
test_scores = 10 * study_hours + np.random.randn(10) * 5

# Prepare Data
X = study_hours.reshape(-1, 1)
y = test_scores

# Train Linear Regression Model
model = LinearRegression()
model.fit(X, y)

print(" Model Learned ")
print(f"Equation: score = {model.coef_[0]:.2f} x hours + {model.intercept_:.2f}")

# Make Predictions
new_data = np.array([[3.5], [6.5], [11]])
predictions = model.predict(new_data)

# Evaluate
y_pred = model.predict(X)
print("Model Performance")
print(f"R^2 score: {r2_score(y, y_pred):.2f}")
print(f"Mean Squared Error: {mean_squared_error(y, y_pred):.2f}")

# Visualize
plt.figure(figsize = (10, 6))
plt.scatter(study_hours, test_scores, color = 'red', s = 100, label = 'Training data', alpha = 0.7)
x_line = np.linspace(0, 12, 100)
y_line = model.predict(x_line.reshape(-1, 1))
plt.plot(x_line, y_line, color = 'blue', linewidth = 2, label = 'Model')
plt.scatter(new_data, predictions, color = 'green', s = 100, marker = 'x', linewidth = 3, label = 'Predictions')
plt.xlabel('Study Hours', fontsize = 12)
plt.ylabel('Test Score', fontsize = 12)
plt.legend()
plt.grid(True, alpha = 0.3)
plt.show()