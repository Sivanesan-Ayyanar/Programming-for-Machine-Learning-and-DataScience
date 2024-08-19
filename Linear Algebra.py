# Importing the necessary library
import numpy as np

# 1. Vectors
print("Vectors:")

# Creating vectors
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print(f"Vector a: {vector_a}")
print(f"Vector b: {vector_b}")

# Vector addition
vector_sum = vector_a + vector_b
print(f"Vector sum (a + b): {vector_sum}")

# Vector subtraction
vector_diff = vector_a - vector_b
print(f"Vector difference (a - b): {vector_diff}")

# Scalar multiplication
scalar = 3
vector_scalar_mult = scalar * vector_a
print(f"Scalar multiplication (3 * a): {vector_scalar_mult}")

# Dot product
dot_product = np.dot(vector_a, vector_b)
print(f"Dot product (a . b): {dot_product}")

# Cross product
cross_product = np.cross(vector_a, vector_b)
print(f"Cross product (a x b): {cross_product}")

# Magnitude of a vector
magnitude_a = np.linalg.norm(vector_a)
print(f"Magnitude of vector a: {magnitude_a}")

print("\n")

# 2. Matrices
print("Matrices:")

# Creating matrices
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

print(f"Matrix A:\n{matrix_A}")
print(f"Matrix B:\n{matrix_B}")

# Matrix addition
matrix_sum = matrix_A + matrix_B
print(f"Matrix sum (A + B):\n{matrix_sum}")

# Matrix subtraction
matrix_diff = matrix_A - matrix_B
print(f"Matrix difference (A - B):\n{matrix_diff}")

# Scalar multiplication
matrix_scalar_mult = scalar * matrix_A
print(f"Scalar multiplication (3 * A):\n{matrix_scalar_mult}")

# Matrix multiplication
matrix_product = np.dot(matrix_A, matrix_B)
print(f"Matrix product (A * B):\n{matrix_product}")

# Transpose of a matrix
matrix_A_transpose = np.transpose(matrix_A)
print(f"Transpose of matrix A:\n{matrix_A_transpose}")

# Determinant of a matrix
matrix_A_determinant = np.linalg.det(matrix_A)
print(f"Determinant of matrix A: {matrix_A_determinant}")

# Inverse of a matrix
matrix_A_inverse = np.linalg.inv(matrix_A)
print(f"Inverse of matrix A:\n{matrix_A_inverse}")

print("\n")

# 3. Solving Linear Equations
print("Solving Linear Equations:")

# Example system of equations:
# 2x + 3y = 5
# 3x + 4y = 7

coefficients = np.array([[2, 3], [3, 4]])
constants = np.array([5, 7])

solution = np.linalg.solve(coefficients, constants)
print(f"Solution for the system of equations:\n{solution}")

print("\n")

# 4. Eigenvalues and Eigenvectors
print("Eigenvalues and Eigenvectors:")

# Eigenvalues and eigenvectors of matrix A
eigenvalues, eigenvectors = np.linalg.eig(matrix_A)

print(f"Eigenvalues of matrix A: {eigenvalues}")
print(f"Eigenvectors of matrix A:\n{eigenvectors}")

print("\n")

# 5. Norms and Orthogonality
print("Norms and Orthogonality:")

# L2 norm of vector a
l2_norm = np.linalg.norm(vector_a)
print(f"L2 norm of vector a: {l2_norm}")

# L1 norm of vector a
l1_norm = np.linalg.norm(vector_a, ord=1)
print(f"L1 norm of vector a: {l1_norm}")

# Checking orthogonality
vector_c = np.array([1, 0, 0])
vector_d = np.array([0, 1, 0])

dot_product_cd = np.dot(vector_c, vector_d)
print(f"Dot product of orthogonal vectors c and d: {dot_product_cd}")
print("Vectors c and d are orthogonal" if dot_product_cd == 0 else "Vectors c and d are not orthogonal")

