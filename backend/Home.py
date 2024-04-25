from flask import Flask, redirect, url_for, request
import Predict as pred
import pandas as pd
from flask_cors import CORS

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
    result = pred.Predict(dataFrame)
    response = {
        'result': f"{result}",
    }

    return response, 200
