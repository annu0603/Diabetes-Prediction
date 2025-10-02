#pip install streamlit
import streamlit as st

# Define the correct password
CORRECT_PASSWORD = "your_password_here"

# Function to authenticate users
def authenticate(password):
    # Compare the provided password with the correct one
    return password == CORRECT_PASSWORD

# Login page
def login_page():
    st.title("Login")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(password):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid password")
    return False

# Main function
def main():
    if login_page():
        # Put your existing code here
        # IMPORT STATEMENTS
        import pandas as pd
        from PIL import Image
        import numpy as np
        import matplotlib.pyplot as plt
        import plotly.figure_factory as ff
        from sklearn.metrics import accuracy_score
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        import seaborn as sns

        # Rest of your code...
        df = pd.read_csv("diabetes.csv")
        # HEADINGS
        st.title('Diabetes Checkup')
        st.sidebar.header('Patient Data')
        st.subheader('Training Data Stats')
        st.write(df.describe())
        # Rest of your code...

# Call the main function
if __name__ == "__main__":
    main()
