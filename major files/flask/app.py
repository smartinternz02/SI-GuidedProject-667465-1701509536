from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    input_data = [float(x) for x in request.form.values()]
    # Make prediction
    prediction = model.predict([input_data])
    if prediction == 1:
        prediction_result = 'Bank is going to get Bankrupt'
    else:
        prediction_result = 'Bank is Not going to get Bankrupt'
    # Render the result template with the prediction and prediction result
    return render_template('result.html', prediction=prediction, prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
