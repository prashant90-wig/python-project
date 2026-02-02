import numpy as np

arr = np.arange(1, 11)

mean = arr.mean()
std = arr.std()
normalized = (arr - mean)/ std

print("Original Array:", arr)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized Array:", normalized)
print("Shape:", normalized.shape)
