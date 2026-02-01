import numpy as np

#Create a 1D Array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D Array:", arr_1d)
print("Shape: ", arr_1d.shape)

#Reshape to 2x3 array
arr_2d = arr_1d.reshape(2,3)
print("\nReshaped to 2x3:")
print(arr_2d)
print("Shape:", arr_2d.shape)

