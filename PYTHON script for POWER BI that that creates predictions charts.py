import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with your dataset path

# Preprocess data
# For demonstration, assume 'X' is the feature and 'Y' is the target variable
X = data[['feature_column']]  # Replace 'feature_column' with your feature column name
Y = data['target_column']     # Replace 'target_column' with your target column name

# Split data into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions
predictions = model.predict(X_test)

# Create prediction chart for 'high', 'medium', 'low'
plt.figure(figsize=(10, 6))
plt.scatter(X_test, Y_test, color='blue', label='Actual')
plt.scatter(X_test, predictions, color='red', label='Predicted')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Prediction Chart')
plt.legend()
plt.show()
