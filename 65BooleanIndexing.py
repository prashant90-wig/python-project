import numpy as np

arr = np.arange(1, 11)

# Create a Boolean mask
mask = arr > 5
print("Boolean Mask:", mask)

# Use the Boolean mask to filter the array
filtered = arr[mask]
print("Filtered Array (elements > 5):", filtered)

