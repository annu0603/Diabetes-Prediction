from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import matplotlib.pyplot as plt
import secrets

# Define your views here
def login(request):
    return render(request, 'login.html')

def login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'your_username' and password == 'your_password':
            request.session['logged_in'] = True  # Securely store login state
            return redirect('upload')  # Redirect to upload page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['dataset']
        if uploaded_file.name != '':
            df = pd.read_csv(uploaded_file)
            return render(request, 'preview.html', {'data': df.to_html(index=False)})
        else:
            messages.error(request, 'Please select a file')
            return redirect('upload')
    return render(request, 'upload.html')

def predict(request):
    if request.method == 'POST':
        # Get user input data and preprocess (if necessary)
        age = float(request.POST.get('age'))
        bmi = float(request.POST.get('bmi'))
        # ... other features
        user_data = pd.DataFrame([[age, bmi, ...]])  # Assuming numerical features
        prediction = predict_diabetes(user_data)
        message = "Diabetic" if prediction == 1 else "Non-diabetic"
        return render(request, 'predict.html', {'prediction': message})
    return render(request, 'predict.html')

def visualize(request):
    # Generate visualizations here
    accuracy = 0.8
    fig, ax = plt.subplots()
    ax.bar(['Accuracy'], [accuracy])
    ax.set_ylabel('Performance')
    plt.savefig('plot.png')
    return render(request, 'visualize.html', {'plot_image': 'plot.png'})

def logout(request):
    request.session.pop('logged_in', None)  # Clear session data on logout
    return redirect('login')
