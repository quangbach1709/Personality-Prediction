from flask import Flask, redirect, url_for, request, jsonify
import pandas as pd
from flask_cors import CORS
import Predict_joblib as predictor

app = Flask(__name__)
CORS(app)

@app.route("/submit", methods=["GET", "POST"])
def PointScale():
    data = request.json

    required_fields = ["Gender", "Age", "E", "A", "C", "N", "O"]
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({"error": f"Missing or null value for {field}"}), 400

    gender = data["Gender"]
    age = int(data["Age"])  # Chuyển đổi age thành số nguyên
    o = int(data["O"])
    n = int(data["N"])
    c = int(data["C"])
    a = int(data["A"])
    e = int(data["E"])
    
    dataFrame = [[gender, age, o, n, c, a, e]]
    
    result = predictor.Predict(dataFrame)
    print("Input data:")
    print(dataFrame)
    print('-------------------///////////////------')
    print("Prediction result:", result)
    response = {
        'result': f"{result}",
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)