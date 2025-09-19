import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_and_save_model():
    # Load the dataset
    df = pd.read_csv('winequality-red.csv', delimiter=';')

    # Define features (X) and target (y)
    X = df.drop('quality', axis=1)
    y = df['quality']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate (optional, for logging)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model trained. Mean Squared Error: {mse}")

    # Save the model to a file
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/model.joblib')
    print("Model saved to 'model/model.joblib'")

if __name__ == '__main__':
    train_and_save_model()