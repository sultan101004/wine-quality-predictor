# Test comment for PR workflow - MLOps Assignment
from flask import Flask, render_template, request
from app.predict import predict_wine_quality

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        data = [float(request.form[field]) for field in [
            'fixed_acidity', 'volatile_acidity', 'citric_acid',
            'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
            'total_sulfur_dioxide', 'density', 'ph', 'sulphates', 'alcohol'
        ]]
        # Make prediction
        prediction = predict_wine_quality(data)
        return render_template('index.html', prediction_text=f'Predicted Wine Quality: {prediction}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)