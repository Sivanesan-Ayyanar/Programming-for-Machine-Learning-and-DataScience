import numpy as np

# 1. Introduction to NumPy
# Importing NumPy with alias 'np'
print("NumPy Tutorial")

# 2. Creating Arrays

# From a Python list
arr = np.array([1, 2, 3])
print("1D Array from list:", arr)

# 2D array from nested lists
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array from nested lists:\n", arr_2d)

# Using built-in functions

# Array of zeros
zeros = np.zeros((3, 3))
print("Array of zeros:\n", zeros)

# Array of ones
ones = np.ones((2, 4))
print("Array of ones:\n", ones)

# Array of a constant value
full = np.full((3, 3), 7)
print("Array of constant value 7:\n", full)

# Array with a range of values
range_arr = np.arange(0, 10, 2)
print("Array with range of values:", range_arr)

# Array with evenly spaced values (linspace)
linspace_arr = np.linspace(0, 1, 5)
print("Array with evenly spaced values:", linspace_arr)

# Identity matrix
identity = np.eye(3)
print("Identity matrix:\n", identity)

# Random array
random_arr = np.random.random((2, 2))
print("Random array:\n", random_arr)

# 3. Array Attributes
print("Shape of arr_2d:", arr_2d.shape)
print("Number of dimensions of arr_2d:", arr_2d.ndim)
print("Data type of arr:", arr.dtype)

# 4. Array Operations

# Arithmetic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

# Universal functions (ufunc)
print("Square root of a:", np.sqrt(a))
print("Exponential of a:", np.exp(a))
print("Sum of elements in a:", np.sum(a))
print("Mean of elements in a:", np.mean(a))

# Matrix operations
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print("Matrix multiplication:\n", np.dot(matrix_a, matrix_b))
print("Element-wise multiplication:\n", matrix_a * matrix_b)

# Transpose of a matrix
print("Transpose of matrix_a:\n", np.transpose(matrix_a))

# 5. Indexing and Slicing

# 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Element at index 2:", arr[2])
print("Slice from index 1 to 3:", arr[1:4])

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, column 2:", arr_2d[1, 2])
print("First two rows:\n", arr_2d[:2])
print("Second column:\n", arr_2d[:, 1])

# Boolean indexing
bool_idx = (arr > 3)
print("Elements greater than 3:", arr[bool_idx])

# 6. Reshaping Arrays
reshaped = np.reshape(arr, (5, 1))
print("Reshaped array:\n", reshaped)

# 7. Stacking Arrays

# Vertical stack
v_stack = np.vstack((a, b))
print("Vertical stack:\n", v_stack)

# Horizontal stack
h_stack = np.hstack((a, b))
print("Horizontal stack:\n", h_stack)

# 8. Splitting Arrays
split_arr = np.split(arr, [2, 4])
print("Split array:", split_arr)

# 9. Copying Arrays

# Shallow copy (view)
shallow_copy = arr.view()
shallow_copy[0] = 10
print("Original array after shallow copy modification:", arr)
print("Shallow copy:", shallow_copy)

# Deep copy
deep_copy = arr.copy()
deep_copy[0] = 1
print("Original array after deep copy modification:", arr)
print("Deep copy:", deep_copy)

# 10. Broadcasting
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
print("Broadcasted addition:\n", x + y)

# 11. Advanced Operations

# Linear algebra
print("Inverse of matrix_a:\n", np.linalg.inv(matrix_a))
print("Eigenvalues of matrix_a:", np.linalg.eig(matrix_a)[0])

# Random sampling
rand_sample = np.random.rand(3, 3)
print("Random sample from uniform distribution:\n", rand_sample)

rand_int = np.random.randint(0, 10, (3, 3))
print("Random integers:\n", rand_int)

# Set seed for reproducibility
np.random.seed(42)
rand_fixed = np.random.rand(2, 2)
print("Fixed random sample:\n", rand_fixed)
