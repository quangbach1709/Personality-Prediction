import pandas as pd
import numpy as np
import joblib

def Predict(dataFinal, predicMethod = "LG"):

	if predicMethod == "LG":
		model = joblib.load('LG.joblib')
	elif predicMethod == "SVC":
		model = joblib.load('SVC.joblib')

	y_pred = model.predict(dataFinal)
	np.zeros((1, 7)).ravel()
	
	personality = ""
	if y_pred[0] == "extraverted":
		personality = "hướng ngoại"
	elif y_pred[0] == "serious":
		personality = "nghiêm túc"
	elif y_pred[0] == "responsible":
		personality = "có trách nhiệm"
	elif y_pred[0] == "lively":
		personality = "hoạt bát"
	elif y_pred[0] == "dependable":
		personality = "đáng tin cậy"

	return personality