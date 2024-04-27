import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.metrics import classification_report
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

train_df = pd.read_csv('train dataset.csv')
train_df.rename(columns = {'Personality (Class label)':'Personality'}, inplace = True)

train_df['Gender'] = train_df['Gender'].apply(lambda x: 1 if x == "Male" else 0)

# Cài đặt mô hình SVM với kernel linear, C = 5
# model = SVC(kernel='linear', C=5)
model = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)

x_train = train_df.drop('Personality', axis=1).values
y_train = train_df['Personality'].values

# Huấn luyện mô hình trên tập dữ liệu huấn luyện
model.fit(x_train, y_train)

#dump model
joblib.dump(model, "LogisticResgression.joblib")
# joblib.dump(model, 'SVC.joblib')