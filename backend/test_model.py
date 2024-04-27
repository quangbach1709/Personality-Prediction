import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

test_df = pd.read_csv('test dataset.csv')
test_df.rename(columns = {'Personality (class label)':'Personality'}, inplace = True)
test_df['Gender'] = test_df['Gender'].apply(lambda x: 1 if x == "Male" else 0)

x_test = test_df.drop('Personality', axis=1).values
y_test = test_df['Personality'].values

model = joblib.load('LogisticResgression.joblib')

y_pred = model.predict(x_test)


# In báo cáo phân loại
print(classification_report(y_test, y_pred))