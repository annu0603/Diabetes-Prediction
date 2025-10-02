# myapp/views.py
from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt

# Define your views here
def login(request):
    return render(request, 'login.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['dataset']
        if uploaded_file.name != '':
            df = pd.read_csv(uploaded_file)
            return render(request, 'preview.html', {'data': df.to_html(index=False)})
        else:
            return HttpResponse('Please select a file')
    return render(request, 'upload.html')

# Define other views similarly

def visualize(request):
    # Generate visualizations here
    accuracy = 0.8
    fig, ax = plt.subplots()
    ax.bar(['Accuracy'], [accuracy])
    ax.set_ylabel('Performance')
    plt.savefig('myapp/static/plot.png')
    return render(request, 'visualize.html', {'plot_image': 'plot.png'})
