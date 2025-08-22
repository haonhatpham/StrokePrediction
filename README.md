# StrokePrediction

Dự án nhỏ trong khuôn khổ khóa học Samsung Innovation Campus (SIC) năm 2025 – lộ trình Data Engineering. Sau khi hoàn thành chương trình, học viên đủ điều kiện sẽ được cấp chứng chỉ. Repo này minh họa một bài toán dự đoán nguy cơ đột quỵ dựa trên dữ liệu sức khỏe, kèm web app demo bằng Streamlit.

## 1. Mục tiêu dự án
- Xây dựng mô hình dự đoán nguy cơ đột quỵ từ các thuộc tính lâm sàng/cá nhân.
- Đóng gói mô hình (Random Forest) và bộ chuẩn hóa (StandardScaler) để suy luận thời gian thực.
- Cung cấp giao diện web đơn giản giúp nhập liệu và xem kết quả dự đoán (Streamlit).

## 1.1. Quy trình (Pipeline)
Hệ thống được triển khai theo pipeline sau (hình minh họa bên dưới):

- Kaggle API: tải dữ liệu gốc từ Kaggle.
- Pandas: tiền xử lý, làm sạch, chọn đặc trưng.
- AWS S3: lưu trữ dữ liệu đã xử lý/đầu ra trung gian.
- scikit-learn: huấn luyện và đánh giá mô hình (RandomForestClassifier,...).
- Matplotlib: trực quan hóa dữ liệu/ROC, hỗ trợ phân tích.

@image1.jpg

## 2. Cấu trúc thư mục
- `app.py`: Ứng dụng Streamlit phục vụ suy luận (inference) trực tiếp từ mô hình đã huấn luyện.
- `model_predict.py`: Pipeline tiền xử lý, chia tập, huấn luyện và đánh giá mô hình (có minh họa SMOTE, StandardScaler, RandomForestClassifier,…).
- `random_forest_model.sav`: Mô hình đã huấn luyện (pickle).
- `scaler.sav`: Bộ chuẩn hóa đặc trưng tương ứng với mô hình (pickle).
- `processed_healthcare_data.csv`: Dữ liệu đã tiền xử lý để huấn luyện/thử nghiệm.
- `requirements.txt`: Danh sách thư viện Python cần thiết.

## 3. Yêu cầu hệ thống
- Python 3.10+ (khuyến nghị)
- pip mới nhất
- Môi trường Windows/macOS/Linux đều hỗ trợ

## 4. Cài đặt nhanh
Khuyến nghị tạo môi trường ảo trước khi cài đặt phụ thuộc.

```bash
python -m venv .venv
# Kích hoạt (Windows)
.venv\Scripts\activate

pip install -r requirements.txt
```

## 5. Chạy ứng dụng web (Streamlit)
```bash
streamlit run app.py
```
Sau khi chạy, trình duyệt sẽ mở giao diện web để nhập thông tin và xem kết quả dự đoán.

### Các trường đầu vào chính (trong `app.py`)
- Age, Average Glucose Level, BMI
- Hypertension, Heart Disease, Ever Married
- Gender, Smoking Status, Work Type, Residence Type

Ứng dụng sẽ chuẩn hóa đầu vào bằng `scaler.sav`, suy luận bằng `random_forest_model.sav`, và hiển thị kết quả/khả năng xảy ra đột quỵ.

## 6. Huấn luyện lại mô hình (tùy chọn)
Nếu muốn tự huấn luyện và đánh giá lại:

```bash
python model_predict.py
```

Ghi chú:
- Script minh họa sử dụng SMOTE để cân bằng dữ liệu và StandardScaler để chuẩn hóa.
- Phần lưu mô hình/scaler đã được minh họa và có thể cần bỏ comment ở cuối file để xuất ra `random_forest_model.sav` và `scaler.sav` mới.
- Đảm bảo `processed_healthcare_data.csv` hiện diện tại thư mục gốc dự án.

### Liên hệ mã nguồn với pipeline
- Tải/chuẩn bị dữ liệu: xem phần đọc `processed_healthcare_data.csv` trong `model_predict.py` (có block S3 mẫu ở dạng comment nếu cần mở rộng lưu trữ).
- Tiền xử lý và cân bằng: `SMOTE`, `StandardScaler` trên tập train.
- Huấn luyện/đánh giá: `RandomForestClassifier`, in các chỉ số `accuracy`, `precision`, `recall`, `f1`, `specificity/sensitivity`, `AUC`, và vẽ ROC bằng `matplotlib`.
- Suy luận thời gian thực: `app.py` tải `random_forest_model.sav` và `scaler.sav`, chuẩn hóa đầu vào rồi dự đoán.

## 7. Lưu ý triển khai
- Đặt `random_forest_model.sav` và `scaler.sav` cùng thư mục với `app.py` khi chạy suy luận.
- Nếu sử dụng AWS S3, thông tin truy cập trong `model_predict.py` chỉ là ví dụ và đã để comment — không commit khóa bí mật thật.

## 8. Thông tin khóa học
Samsung Innovation Campus 2025 – Data Engineering: chương trình đào tạo kỹ năng thực hành về thu thập, xử lý, lưu trữ, phân tích dữ liệu và triển khai mô hình. Học viên hoàn thành yêu cầu đầu ra sẽ nhận chứng chỉ do chương trình cấp.
