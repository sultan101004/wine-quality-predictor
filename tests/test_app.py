import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Wine Quality Prediction" in response.data

def test_predict_endpoint(client):
    # Test a valid prediction
    data = {
        'fixed_acidity': 7.4, 'volatile_acidity': 0.7, 'citric_acid': 0.0,
        'residual_sugar': 1.9, 'chlorides': 0.076, 'free_sulfur_dioxide': 11.0,
        'total_sulfur_dioxide': 34.0, 'density': 0.9978, 'ph': 3.51,
        'sulphates': 0.56, 'alcohol': 9.4
    }
    response = client.post('/predict', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Predicted Wine Quality" in response.data