import pytest
from app.predict import predict_wine_quality

def test_predict_wine_quality():
    # Create a sample input of 11 features
    sample_features = [7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]
    prediction = predict_wine_quality(sample_features)
    # We can't know the exact value, but we can check it's a number
    assert isinstance(prediction, float)
    assert 0 <= prediction <= 10  # Quality should be roughly between 0 and 10