from django.shortcuts import render
from django.conf import settings
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    csv_file_path = os.path.join(settings.BASE_DIR, "diabetes.csv")

    # Read the CSV file
    data = pd.read_csv(csv_file_path)
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    prgnencies = float(request.GET.get('n1', 0))  # Replace 0 with your default value if needed
    glucose = float(request.GET.get('n2', 0))
    blood_pressure = float(request.GET.get('n3', 0))
    skin_thickness = float(request.GET.get('n4', 0))
    insulin = float(request.GET.get('n5', 0))
    bmi = float(request.GET.get('n6', 0))
    diabetes_pedigree = float(request.GET.get('n7', 0))
    age = float(request.GET.get('n8', 0))

    # Your logic for processing the parameters goes here

    # Assuming 'model' is your trained machine learning model
    pred = model.predict([[prgnencies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])

    result = ""
    if pred==[1]:
        result = "Detected! Positive"
    else:
        result = "Detected! Negative"
    return render(request, 'predict.html', {"result": result})