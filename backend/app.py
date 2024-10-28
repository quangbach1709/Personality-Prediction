import pandas as pd  # Nhập thư viện pandas để xử lý dữ liệu dạng
from numpy import *  # Nhập tất cả các hàm từ thư viện numpy
import numpy as np  # Nhập thư viện numpy với tên viết tắt np
from sklearn.neighbors import KNeighborsClassifier  # Nhập lớp KNeighborsClassifier từ thư viện sklearn
from sklearn.tree import DecisionTreeClassifier  # Nhập lớp DecisionTreeClassifier từ thư viện sklearn
from sklearn.svm import SVC  # Nhập lớp SVC từ thư viện sklearn
from sklearn.ensemble import RandomForestClassifier  # Nhập lớp RandomForestClassifier từ thư viện sklearn
from sklearn.linear_model import LogisticRegression  # Nhập lớp LogisticRegression từ thư viện sklearn
from sklearn import datasets, linear_model  # Nhập các module datasets và linear_model từ sklearn
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score  # Nhập các hàm đánh giá từ sklearn
from sklearn import metrics  # Nhập module metrics từ sklearn
from sklearn.model_selection import train_test_split  # Nhập hàm train_test_split để chia dữ liệu
from sklearn.metrics import f1_score  # Nhập hàm f1_score từ sklearn
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score  # Nhập các hàm đánh giá khác
import matplotlib.pyplot as plt  # Nhập thư viện matplotlib để vẽ đồ thị
import seaborn as sns  # Nhập thư viện seaborn để vẽ đồ thị đẹp hơn

data = pd.read_csv('train dataset.csv')  # Đọc dữ liệu từ file CSV vào DataFrame
array = data.values  # Chuyển đổi DataFrame thành mảng numpy

for i in range(len(array)):  # Lặp qua từng hàng trong mảng
    if array[i][0] == "Male":  # Kiểm tra giới tính
        array[i][0] = 1  # Nếu là "Male", gán giá trị 1
    else:
        array[i][0] = 0  # Nếu không, gán giá trị 0

df = pd.DataFrame(array)  # Chuyển đổi mảng trở lại thành DataFrame

maindf = df[[0, 1, 2, 3, 4, 5, 6]]  # Chọn các cột cần thiết từ DataFrame
mainarray = maindf.values  # Chuyển đổi DataFrame thành mảng numpy

temp = df[7]  # Lấy cột thứ 8 (cột nhãn) từ DataFrame
train_y = temp.values  # Chuyển đổi cột nhãn thành mảng numpy

for i in range(len(train_y)):  # Lặp qua từng giá trị trong mảng nhãn
    train_y[i] = str(train_y[i])  # Chuyển đổi giá trị thành chuỗi

model = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg', max_iter=1000)  # Khởi tạo mô hình hồi quy logistic
# model = KNeighborsClassifier(n_neighbors=5, metric='manhattan')  # Mô hình KNN (bị chú thích)
# model = RandomForestClassifier(n_estimators=1000, min_samples_split=5, min_samples_leaf=8, min_impurity_decrease=0.1)  # Mô hình Random Forest (bị chú thích)
# model = DecisionTreeClassifier(max_leaf_nodes=5)  # Mô hình Decision Tree (bị chú thích)
# model = SVC(kernel='linear', C=0.1)  # Mô hình SVM (bị chú thích)
model.fit(mainarray, train_y)  # Huấn luyện mô hình với dữ liệu huấn luyện

testdata = pd.read_csv('test dataset.csv')  # Đọc dữ liệu kiểm tra từ file CSV
test = testdata.values  # Chuyển đổi DataFrame kiểm tra thành mảng numpy

for i in range(len(test)):  # Lặp qua từng hàng trong mảng kiểm tra
    if test[i][0] == "Male":  # Kiểm tra giới tính
        test[i][0] = 1  # Nếu là "Male", gán giá trị 1
    else:
        test[i][0] = 0  # Nếu không, gán giá trị 0

df1 = pd.DataFrame(test)  # Chuyển đổi mảng kiểm tra trở lại thành DataFrame

testdf = df1[[0, 1, 2, 3, 4, 5, 6]]  # Chọn các cột cần thiết từ DataFrame kiểm tra
y_testdf = df1[7].values  # Lấy cột nhãn từ DataFrame kiểm tra
maintestarray = testdf.values  # Chuyển đổi DataFrame kiểm tra thành mảng numpy

y_pred = model.predict(maintestarray)  # Dự đoán nhãn cho dữ liệu kiểm tra

for i in range(len(y_pred)):  # Lặp qua từng giá trị dự đoán
    y_pred[i] = str((y_pred[i]))  # Chuyển đổi giá trị dự đoán thành chuỗi
DF = pd.DataFrame(y_pred, columns=['Predicted Personality'])  # Tạo DataFrame từ mảng dự đoán
DF.index = DF.index + 1  # Đặt lại chỉ số bắt đầu từ 1
DF.index.names = ['Person No']  # Đặt tên cho chỉ số
DF.to_csv("output.csv")  # Xuất DataFrame dự đoán ra file CSV

accuracy = accuracy_score(y_testdf, y_pred)  # Tính độ chính xác của mô hình
matrix = confusion_matrix(y_testdf, y_pred)  # Tính ma trận nhầm lẫn
percision_macro = precision_score(y_testdf, y_pred, average='macro')  # Tính độ chính xác macro
percision_weighted = precision_score(y_testdf, y_pred, average='weighted')  # Tính độ chính xác weighted
recall_macro = recall_score(y_testdf, y_pred, average='macro')  # Tính độ nhạy macro
recall_weighted = recall_score(y_testdf, y_pred, average='weighted')  # Tính độ nhạy weighted
f1_macro = f1_score(y_testdf, y_pred, average='macro')  # Tính F1-score macro
f1_weighted = f1_score(y_testdf, y_pred, average='weighted')  # Tính F1-score weighted



print("Accuracy:", accuracy)  # In độ chính xác
print("Macro avg of Precision:", percision_macro)  # In độ chính xác macro
print("Macro avg of Recall:", recall_macro)  # In độ nhạy macro
print("Macro avg of F1-score:", f1_macro)  # In F1-score macro


print("Weighted avg of Precision:", percision_weighted)  # In độ chính xác weighted
print("Weighted avg of Recall:", recall_weighted)  # In độ nhạy weighted
print("Weighted avg of F1-score:", f1_weighted)  # In F1-score weighted
print("Matrix:\n", matrix)  # In ma trận nhầm lẫn

# Tạo biểu đồ confusion matrix
plt.figure(figsize=(8, 6))  # Tạo một hình với kích thước 8x6 inch
sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y_testdf), yticklabels=np.unique(y_testdf))  # Vẽ biểu đồ nhiệt cho ma trận nhầm lẫn
plt.xlabel('Predicted Labels')  # Đặt nhãn cho trục x
plt.ylabel('True Labels')  # Đặt nhãn cho trục y
plt.title('Confusion Matrix')  # Đặt tiêu đề cho biểu đồ
plt.show()  # Hiển thị biểu đồ
