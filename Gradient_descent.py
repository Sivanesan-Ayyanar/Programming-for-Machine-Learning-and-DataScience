import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:\Users\vs632\Downloads\Salary_data.csv'
data = pd.read_csv(file_path)

# Check for missing values
print("Missing values in each column:")
print(data.isnull().sum())

# Handling missing values by dropping rows with NaN values
data = data.dropna()

# Convert columns to numeric (in case there are non-numeric values)
data['X'] = pd.to_numeric(data['X'], errors='coerce')
data['Y'] = pd.to_numeric(data['Y'], errors='coerce')

# Re-check for any NaN after conversion and drop them
data = data.dropna()

# Extracting X and Y values
x = data['X'].values
y = data['Y'].values

# Normalize the data to prevent overflow during gradient descent
x_mean = np.mean(x)
x_std = np.std(x)
x = (x - x_mean) / x_std

y_mean = np.mean(y)
y_std = np.std(y)
y = (y - y_mean) / y_std

n = np.size(x)

# Gradient Descent Parameters
alpha = 0.001  # Reduced learning rate
iterations = 1000  # Number of iterations

# Initialize parameters
theta0 = 0
theta1 = 0

# Gradient Descent Algorithm
for i in range(iterations):
    y_pred = theta1 * x + theta0
    error = y_pred - y

    # Compute cost
    cost = (1 / (2 * n)) * np.sum(error ** 2)

    # Compute gradients
    d_theta0 = (1 / n) * np.sum(error)
    d_theta1 = (1 / n) * np.sum(error * x)

    # Update parameters
    theta0 = theta0 - alpha * d_theta0
    theta1 = theta1 - alpha * d_theta1

    # Print cost and parameters at specified iterations
    if i % 100 == 0:
        print(f"Iteration {i}: Cost = {cost:.4f}, θ0 = {theta0:.4f}, θ1 = {theta1:.4f}")

# Revert normalization for final parameters
theta1 = theta1 * y_std / x_std
theta0 = theta0 * y_std + y_mean - theta1 * x_mean

# Predicted values using the final parameters
y_pred = theta1 * x * x_std + theta0

# Scatter plot of the data
plt.scatter(x * x_std + x_mean, y * y_std + y_mean, color='red', label='Original data')
plt.plot(x * x_std + x_mean, y_pred, color='green', label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Line with Gradient Descent')
plt.legend()
plt.show()

# Print final parameters
print('Final Slope θ1:', theta1)
print('Final Intercept θ0:', theta0)

# Calculating the error
error = y - y_pred

# Calculating squared error
se = np.sum(error ** 2)
print('Squared Error is:', se)

# Calculating mean squared error
mse = se / n
print('Mean Squared Error (MSE) is:', mse)

# Calculating root mean squared error
rmse = np.sqrt(mse)
print('Root Mean Squared Error (RMSE) is:', rmse)

# Calculating mean absolute error
mae = np.mean(np.abs(error))
print('Mean Absolute Error (MAE) is:', mae)

# Calculating R-squared
ss_total = np.sum((y * y_std + y_mean - y_mean) ** 2)
ss_residual = np.sum((y * y_std + y_mean - y_pred) ** 2)
r_squared = 1 - (ss_residual / ss_total)
print('R² Score is:', r_squared)
