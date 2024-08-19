import numpy as np
import matplotlib.pyplot as plt

# Input data
x = np.array([1, 2, 3, 4, 5])
y = np.array([7, 14, 15, 18, 19])

# Add a column of ones to X (to account for θ0)
X = np.c_[np.ones(x.shape[0]), x]  # X becomes a 2D array with a column of ones and x values

# Compute the parameters using the Normal Equation
theta = np.linalg.inv(X.T @ X) @ X.T @ y

# Extract θ0 and θ1 from the theta vector
theta0, theta1 = theta[0], theta[1]

print('Computed θ0 (intercept):', theta0)
print('Computed θ1 (slope):', theta1)

# Predicted values using the computed parameters
y_pred = theta1 * x + theta0
print("Predicted Y values:", y_pred)

# Plotting the regression line
plt.scatter(x, y, color='red', label='Original data')
plt.plot(x, y_pred, color='green', label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression using Normal Equation')
plt.legend()
plt.show()
