import numpy as np
import pandas as pd
import pickle

# Load the scaler and classifier separately
scaler = pickle.load(open('model/scaler.pkl', 'rb'))  # Load the scaler
classifier = pickle.load(open('model/svm_model.pkl', 'rb'))  # Load the trained classifier

print("Model and Scaler loaded successfully.")

# Input data for prediction (this is a new test instance)
input_data = (6,148,72,35,0,33.6,0.627,50)

# Convert the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array for a single instance (as the model expects input shape [1, -1])
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Define column names for the input data (same as during training)
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Create a DataFrame with the input data and the same column names
input_data_df = pd.DataFrame(input_data_reshaped, columns=columns)

# Standardize the input data using the loaded scaler
std_data = scaler.transform(input_data_df)

# Make a prediction using the loaded classifier
prediction = classifier.predict(std_data)

# Print the prediction result
if prediction[0] == 0:
    print("The person is not diabetic")
else:
    print("The person is diabetic")
