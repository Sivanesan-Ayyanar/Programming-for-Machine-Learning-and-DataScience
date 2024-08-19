import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load data from CSV file
file_path = r"C:\Users\vs632\Downloads\Salary_data.csv"  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Check for missing values
print("Missing values in the dataset:\n", data.isna().sum())

# Drop rows with missing values
data = data.dropna()

# Extract X and Y from the DataFrame
x = data[['X']].values  # Replace 'X_column_name' with the name of the X column in your CSV
y = data['Y'].values    # Replace 'Y_column_name' with the name of the Y column in your CSV

# Calculate mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

print('Mean of X:', mean_x)
print('Mean of Y:', mean_y)

# Create a LinearRegression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Get the slope (θ1) and intercept (θ0)
theta1 = model.coef_[0]
theta0 = model.intercept_

print('Computed θ0 (intercept):', theta0)
print('Computed θ1 (slope):', theta1)

# Predict the y values using the model
y_pred = model.predict(x)
print("Predicted Y values:", y_pred)

# Plotting the regression line
plt.scatter(x, y, color='red', label='Original data')
plt.plot(x, y_pred, color='green', label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression using scikit-learn')
plt.legend()
plt.show()

# Evaluation Metrics
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f'Mean Squared Error (MSE): {mse:.4f}')
print(f'Root Mean Squared Error (RMSE): {rmse:.4f}')
print(f'Mean Absolute Error (MAE): {mae:.4f}')
print(f'R² Score: {r2:.4f}')
