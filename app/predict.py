import joblib
import numpy as np

# Load the model once when this module is imported
model = joblib.load('model/model.joblib')

def predict_wine_quality(features):
    """
    Predict wine quality based on input features.
    Features must be a list in the correct order.
    """
    # Convert features to a numpy array and reshape for a single sample
    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)
    return round(prediction[0], 2)