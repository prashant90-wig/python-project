import numpy as np

#Set seed for reproducibility
np.random.seed(42)

#Create a 3x3 matrix with random floats between 0 and 1
matrix = np.random.rand(3, 3)
print("\nRandom 3x3 Matrix:")
print(matrix)
print("Shape:", matrix.shape)

#Find the maximum and minimum values
max_value = matrix.max()
min_value = matrix.min()

#Find their positions
max_pos = np.unravel_index(matrix.argmax(), matrix.shape)
min_pos = np.unravel_index(matrix.argmin(), matrix.shape)

print(f"\nMaximum Value: {max_value:.4f} at position {max_pos}")
print(f"Minimum Value: {min_value:.4f} at position {min_pos}")

#Random Integer Matrix
random_ints = np.random.randint(0, 100, size=(3,3))
print("\nRandom 3x3 Integer Matrix:")
print(random_ints)
print("Shape:", random_ints.shape)
