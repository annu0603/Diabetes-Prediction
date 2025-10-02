# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Global variables for dataset and model
dataset = None
model = None

# Landing Page - Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check login credentials
        # Redirect to dataset upload page if login is successful
        return redirect(url_for('upload_dataset'))
    return render_template('login.html')

# Dataset Upload Page
@app.route('/upload_dataset', methods=['GET', 'POST'])
def upload_dataset():
    global dataset
    if request.method == 'POST':
        # Get uploaded file
        uploaded_file = request.files['diabetes']
        # Read CSV file
        dataset = pd.read_csv(uploaded_file)
        # Show preview
        return render_template('preview.html', data=dataset.head())
    return render_template('upload.html')

# Train SVM model
def train_model():
    global dataset
    global model
    X = dataset.drop(columns=['target_column'])
    y = dataset['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)

# Diabetes Prediction
# Diabetes Prediction
@app.route('/predict_diabetes', methods=['GET', 'POST'])
def predict_diabetes():
    global model
    if request.method == 'POST':
        # Get input from user
        preg = float(request.form['pregnancies'])
        glu = float(request.form['glucose'])
        bp = float(request.form['blood_pressure'])
        skin = float(request.form['skin_thickness'])
        ins = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['diabetes_pedigree_function'])
        age = float(request.form['age'])
        
        # Perform prediction
        user_input = [[preg, glu, bp, skin, ins, bmi, dpf, age]]
        prediction = model.predict(user_input)
        
        # Return prediction result
        return render_template('predict.html', prediction=prediction[0])
    return render_template('predict.html')


# Visualization Page
# Visualization Page
@app.route('/visualization')
def visualize():
    global model
    global dataset
    
    if model is None or dataset is None:
        return "Model or dataset not available"
    
    # Split the dataset into features and target
    X = dataset.drop(columns=['target_column'])
    y = dataset['target_column']
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, model.predict(X_test))
    
    # Generate a plot
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test['feature_1'], X_test['feature_2'], c=y_test, cmap='viridis', s=50, alpha=0.5)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Model Prediction (Accuracy: {:.2f}%)'.format(accuracy * 100))
    plt.grid(True)
    
    # Save visualization to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return '<img src="data:image/png;base64,{}">'.format(plot_url)


if __name__ == '__main__':
    # Example dataset path, replace with your actual path
    dataset_path = 'diabetes.csv'
    dataset = pd.read_csv(dataset_path)
    
    train_model()  # Train the model when the application starts
    app.run(debug=True)
