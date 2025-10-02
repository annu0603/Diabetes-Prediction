# Import necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define the correct login credentials
CORRECT_EMAIL = "your_email_here"
CORRECT_PASSWORD = "your_password_here"

# Function to authenticate users
def authenticate(email, password):
    return email == CORRECT_EMAIL and password == CORRECT_PASSWORD

# Function for login page
def login_page():
    st.title("Diabetes Prediction - Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(email, password):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid email or password")
    return False

# Function to upload dataset
def upload_dataset():
    st.title("Upload Dataset")
    st.write("Please upload your dataset (CSV file)")
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        return df
    return None

# Function for diabetes prediction
def diabetes_prediction(df):
    st.title("Diabetes Prediction")
    if df is not None:
        st.subheader("Enter Patient Information")
        pregnancies = st.slider("Pregnancies", 0, 17, 3)
        glucose = st.slider("Glucose", 0, 200, 120)
        blood_pressure = st.slider("Blood Pressure", 0, 122, 70)
        skin_thickness = st.slider("Skin Thickness", 0, 100, 20)
        insulin = st.slider("Insulin", 0, 846, 79)
        bmi = st.slider("BMI", 0.0, 67.0, 20.0)
        dpf = st.slider("Diabetes Pedigree Function", 0.0, 2.4, 0.47)
        age = st.slider("Age", 21, 88, 33)

        user_data = pd.DataFrame({
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [dpf],
            "Age": [age]
        })

        st.write("User Input:")
        st.write(user_data)

        # Train the model
        X = df.drop("Outcome", axis=1)
        y = df["Outcome"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Make prediction
        prediction = model.predict(user_data)
        st.subheader("Prediction")
        if prediction[0] == 0:
            st.write("No diabetes detected.")
        else:
            st.write("Diabetes detected.")

# Function for visualization
def visualization(df):
    st.title("Visualization")
    if df is not None:
        st.subheader("Model Evaluation")
        X = df.drop("Outcome", axis=1)
        y = df["Outcome"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write("Accuracy:", accuracy)

# Main function
def main():
    if not login_page():
        return

    dataset = upload_dataset()
    if dataset is None:
        st.warning("Please upload a dataset.")
        return

    diabetes_prediction(dataset)
    visualization(dataset)

if __name__ == "__main__":
    main()
