import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv(r'C:\Users\vs632\Downloads\Salary_data.csv')

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
n = np.size(x)

# Scatter plot of the data
plt.scatter(x, y, color='red')
plt.xlabel('Independent variable X')
plt.ylabel('Dependent variable Y')
plt.title('Scatter Plot of X vs Y')
plt.show()

# Mean of X and Y
x_mean = np.mean(x)
y_mean = np.mean(y)
print("Mean of X:", x_mean)
print("Mean of Y:", y_mean)

# Calculating the slope (θ1)
num = np.sum((x - x_mean) * (y - y_mean))
den = np.sum((x - x_mean) ** 2)
theta1 = num / den
print('Slope θ1 is:', theta1)

# Calculating the intercept (θ0)
theta0 = y_mean - theta1 * x_mean
print('Intercept θ0 is:', theta0)

# Prediction using the linear model
y_pred = theta1 * x + theta0
print("Predicted Y values:", y_pred)

# Plotting the regression line
plt.scatter(x, y, color='red', label='Original data')
plt.plot(x, y_pred, color='green', label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Line')
plt.legend()
plt.show()

# Calculating the error
error = y - y_pred
print("Error:", error)

# Calculating squared error
se = np.sum(error ** 2)
print('Squared Error is:', se)

# Calculating mean squared error
mse = se / n
print('Mean Squared Error is:', mse)
