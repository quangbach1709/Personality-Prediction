import pandas as pd
from numpy import *
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

def Predict(dataFinal):
	data =pd.read_csv('train dataset.csv')
	array = data.values

	for i in range(len(array)):
		if array[i][0]=="Male":
			array[i][0]=1
		else:
			array[i][0]=0

	df=pd.DataFrame(array)

	maindf =df[[0,1,2,3,4,5,6]]
	mainarray=maindf.values
	# print (mainarray)

	temp=df[7]
	train_y =temp.values
	# print(train_y)
	# print(mainarray)
	train_y=temp.values

	for i in range(len(train_y)):
		train_y[i] =str(train_y[i])

	model = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
	# model = KNeighborsClassifier(n_neighbors=5, metric='manhattan')
	#model = RandomForestClassifier(n_estimators=1000, min_samples_split = 5, min_samples_leaf = 8, min_impurity_decrease = 0.1)
	#model = DecisionTreeClassifier(max_leaf_nodes=5)
	# model = SVC(kernel='linear',C=5)
	model.fit(mainarray, train_y)

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

