import streamlit as st
import pickle
import numpy as np

# Tải mô hình đã huấn luyện và bộ chuẩn hóa
model = pickle.load(open('random_forest_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

# Hàm để dự đoán đột quỵ
def predict_stroke(features):
    features = np.array(features).reshape(1, -1)
    features_std = scaler.transform(features)
    prediction = model.predict(features_std)
    probability = model.predict_proba(features_std)[0][1]
    return prediction, probability

# Giao diện người dùng Streamlit
def main():
    st.title("Stroke Prediction Web App")
    st.write("Enter the required information to predict the likelihood of stroke.")

    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    hypertension = st.selectbox("Hypertension", ("Yes", "No"))
    heart_disease = st.selectbox("Heart Disease", ("Yes", "No"))
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=80.0)
    bmi = st.number_input("BMI", min_value=0.0, value=20.0)
    gender = st.selectbox("Gender", ("Male", "Female"))
    smoking_status = st.selectbox("Smoking Status", ("Unknown", "Formerly Smoked", "Never Smoked", "Smokes"))
    ever_married = st.selectbox("Ever Married", ("Yes", "No"))
    work_type = st.selectbox("Work Type", ("Private", "Self-employed", "Children", "Govt_job", "Never_worked"))
    residence_type = st.selectbox("Residence Type", ("Urban", "Rural"))

    # Chuyển đổi gia trị đầu vào thành định dạng số
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0
    gender = 1 if gender == "Male" else 0
    ever_married = 1 if ever_married == "Yes" else 0
    residence_type = 1 if residence_type == "Urban" else 0

    smoking_map = {
        "Unknown": 0,
        "Formerly Smoked": 1,
        "Never Smoked": 2,
        "Smokes": 3
    }
    smoking_status = smoking_map[smoking_status]

    work_type_map = {
        "Govt_job": 0,
        "Never_worked": 1,
        "Private": 2,
        "Self-employed": 3,
        "Children": 4,
    }
    work_type = work_type_map[work_type]

    if st.button("Predict Stroke"):
        features = [gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]
        prediction, probability = predict_stroke(features)
        if prediction[0] == 0:
            st.success("Congratulations! You have a low risk of stroke.")
        else:
            st.error("Warning! You are at a high risk of stroke.")
            st.write("Probability of stroke: {:.2f}".format(probability))

#Hàm main
if __name__ == "__main__":
    main()
