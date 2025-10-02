import pandas as pd
from sklearn.svm import SVC  # Using SVM with linear kernel

# Load your pre-trained diabetes prediction model (replace with your model training logic)
def load_model():
    try:
        # Load the model from a secure location (e.g., outside script directory)
        with open('diabetes_model.pkl', 'rb') as f:
            model = joblib.load(f)
        return model
    except FileNotFoundError:
        raise Exception('Model not found. Please train a model first.')

def predict_diabetes(data):
    model = load_model()
    # Preprocess user input data (if necessary) based on your model's requirements
    # ...
    prediction = model.predict(data)[0]  # Assuming single prediction
    return prediction
