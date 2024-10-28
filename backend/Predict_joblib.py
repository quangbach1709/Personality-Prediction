import pandas as pd  # Nhập thư viện pandas để xử lý dữ liệu dạng bảng
import numpy as np  # Nhập thư viện numpy để xử lý các mảng và tính toán số học
from sklearn.linear_model import LogisticRegression  # Nhập lớp LogisticRegression từ thư viện sklearn để xây dựng mô hình hồi quy logistic
from sklearn.svm import SVC  # Nhập lớp SVC từ thư viện sklearn để xây dựng mô hình SVM
from sklearn.preprocessing import StandardScaler  # Nhập lớp StandardScaler để chuẩn hóa dữ liệu
from sklearn.impute import SimpleImputer  # Nhập lớp SimpleImputer để xử lý giá trị thiếu

# Hàm này load và tiền xử lý dữ liệu
def load_and_preprocess_data():
    # Đọc dữ liệu huấn luyện từ file CSV
    train_data = pd.read_csv('train dataset.csv')
    
    # Tách features (X_train) và target (y_train)
    X_train = train_data[['Gender', 'Age', 'openness', 'neuroticism', 'conscientiousness', 'agreeableness', 'extraversion']]  # Chọn các cột đặc trưng
    y_train = train_data['Personality (Class label)']  # Chọn cột nhãn

    # Mã hóa biến categorical 'Gender'
    gender_map = {'Male': 0, 'Female': 1}  # Tạo từ điển ánh xạ giới tính
    X_train['Gender'] = X_train['Gender'].map(gender_map)  # Ánh xạ giới tính thành số

    # Xử lý giá trị thiếu bằng cách điền giá trị trung bình
    imputer = SimpleImputer(strategy='mean')  # Khởi tạo bộ xử lý giá trị thiếu với chiến lược điền giá trị trung bình
    X_train_imputed = imputer.fit_transform(X_train)  # Điền giá trị thiếu trong dữ liệu huấn luyện

    # Chuẩn hóa các features số
    scaler = StandardScaler()  # Khởi tạo bộ chuẩn hóa
    X_train_scaled = scaler.fit_transform(X_train_imputed)  # Chuẩn hóa dữ liệu đã xử lý

    return X_train_scaled, y_train, imputer, scaler  # Trả về dữ liệu đã chuẩn hóa, nhãn, bộ xử lý giá trị thiếu và bộ chuẩn hóa

# Hàm này huấn luyện các mô hình
def train_models():
    X_train_scaled, y_train, _, _ = load_and_preprocess_data()  # Gọi hàm load_and_preprocess_data để lấy dữ liệu đã chuẩn hóa và nhãn

    # Huấn luyện mô hình Logistic Regression
    lr_model = LogisticRegression(random_state=42, max_iter=1000)  # Khởi tạo mô hình hồi quy logistic
    lr_model.fit(X_train_scaled, y_train)  # Huấn luyện mô hình với dữ liệu đã chuẩn hóa

    # Huấn luyện mô hình SVM
    svm_model = SVC(random_state=42, probability=True)  # Khởi tạo mô hình SVM
    svm_model.fit(X_train_scaled, y_train)  # Huấn luyện mô hình với dữ liệu đã chuẩn hóa

    return lr_model, svm_model  # Trả về hai mô hình đã huấn luyện

# Hàm chính để dự đoán tính cách
def Predict(dataFinal, predicMethod="LG"):
    # Load và tiền xử lý dữ liệu
    _, _, imputer, scaler = load_and_preprocess_data()  # Gọi hàm load_and_preprocess_data để lấy bộ xử lý giá trị thiếu và bộ chuẩn hóa

    # Tiền xử lý dữ liệu đầu vào
    columns = ['Gender', 'Age', 'openness', 'neuroticism', 'conscientiousness', 'agreeableness', 'extraversion']  # Định nghĩa các cột
    dataFinal = pd.DataFrame(dataFinal, columns=columns)  # Chuyển đổi dữ liệu đầu vào thành DataFrame

    # In ra dữ liệu đầu vào trước khi xử lý
    print("Input data before processing:")  # In thông báo
    print(dataFinal.to_dict(orient='records'))  # In dữ liệu đầu vào dưới dạng từ điển

    # Mã hóa giá trị 'Gender' nếu cần
    if dataFinal['Gender'].dtype == object:  # Kiểm tra kiểu dữ liệu của cột 'Gender'
        gender_map = {'Male': 0, 'Female': 1}  # Tạo từ điển ánh xạ giới tính
        dataFinal['Gender'] = dataFinal['Gender'].map(gender_map)  # Ánh xạ giới tính thành số

    # Xử lý giá trị thiếu trong dữ liệu đầu vào
    dataFinal_imputed = imputer.transform(dataFinal)  # Điền giá trị thiếu trong dữ liệu đầu vào

    # Chuẩn hóa dữ liệu đầu vào
    dataFinal_scaled = scaler.transform(dataFinal_imputed)  # Chuẩn hóa dữ liệu đầu vào đã xử lý

    # Huấn luyện các mô hình
    lr_model, svm_model = train_models()  # Gọi hàm train_models để huấn luyện các mô hình

    # Thực hiện dự đoán
    if predicMethod == "LG":  # Kiểm tra phương pháp dự đoán
        y_pred = lr_model.predict(dataFinal_scaled)  # Dự đoán với mô hình hồi quy logistic
    elif predicMethod == "SVC":  # Nếu phương pháp là SVC
        y_pred = svm_model.predict(dataFinal_scaled)  # Dự đoán với mô hình SVM
    else:  # Nếu phương pháp không hợp lệ
        raise ValueError("Invalid prediction method. Use 'LG' or 'SVC'.")  # Ném lỗi

    print("Input data after processing:")  # In thông báo
    print(dataFinal.to_dict(orient='records'))  # In dữ liệu đầu vào sau khi xử lý
    print("--------------|||||||||||||||||||||||||||||------")  # In dấu phân cách
    print(y_pred)  # In kết quả dự đoán

    # Ánh xạ kết quả dự đoán sang tiếng Việt
    personality_map = {  # Tạo từ điển ánh xạ kết quả dự đoán sang tiếng Việt
        "extraverted": "Hướng ngoại",
        "serious": "Nghiêm túc",
        "responsible": "Có trách nhiệm",
        "lively": "Hoạt bát",
        "dependable": "Đáng tin cậy"
    }

    personality = personality_map.get(y_pred[0], "Unknown")  # Ánh xạ kết quả dự đoán sang tiếng Việt

    print(personality)  # In kết quả dự đoán
    return personality  # Trả về kết quả dự đoán

# Hàm kiểm tra dự đoán
def test_prediction():
    test_data = [['Male',18,5,7,7,6,4]]  # Dữ liệu kiểm tra
    result = Predict(test_data, "SVC")  # Gọi hàm Predict để dự đoán
    print(f"Test prediction result: {result}")  # In kết quả dự đoán

# Uncomment dòng dưới đây để chạy hàm kiểm tra
test_prediction()  # Gọi hàm kiểm tra