from flask import Flask, redirect, url_for, request
import pandas as pd
from flask_cors import CORS
import Predict_joblib as predictor

app = Flask(__name__)
CORS(app)

@app.route("/submit", methods = ["GET", "POST"])
def PointScale():

    data = request.json

    gender = data["Gender"]
    age = data["Age"]
    e = data["E"]
    a = data["A"]
    c = data["C"]
    n = data["N"]
    o = data["O"]
    
    dataFrame = [[gender, age, o, n, c, a, e]]
    result = predictor.Predict(dataFrame)
    response = {
        'result': f"{result}",
    }

    return response, 200
