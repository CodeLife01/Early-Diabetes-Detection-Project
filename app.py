import streamlit as st
import numpy as np
import pickle
import warnings
import os
warnings.filterwarnings("ignore")

# Load the trained model and StandardScaler
MODEL_PATH = "2. Model/diabetes_model.pkl"

# Check if file exists before loading
if os.path.exists(MODEL_PATH):
    model = pickle.load(open(MODEL_PATH, "rb"))
else:
    st.error(f"Model file not found: {MODEL_PATH}. Check your file path!")
scaler = pickle.load(open("2. Model/scaler.pkl", "rb"))

# Streamlit UI
st.title("🔍 Early Diabetes Detection App")
st.write("Fill in the details below to predict the risk of diabetes.")

# User Input Form
age = st.number_input("Enter Age:", min_value=20, max_value=65, value=30)
gender = st.radio("Select Gender:", ["Male", "Female"])
polyuria = st.radio("Polyuria (Excessive Urination):", ["Yes", "No"])
polydipsia = st.radio("Polydipsia (Excessive Thirst):", ["Yes", "No"])
sudden_weight_loss = st.radio("Sudden Weight Loss:", ["Yes", "No"])
weakness = st.radio("Weakness:", ["Yes", "No"])
polyphagia = st.radio("Polyphagia (Excessive Hunger):", ["Yes", "No"])
genital_thrush = st.radio("Genital Thrush:", ["Yes", "No"])
visual_blurring = st.radio("Visual Blurring:", ["Yes", "No"])
itching = st.radio("Itching:", ["Yes", "No"])
irritability = st.radio("Irritability:", ["Yes", "No"])
delayed_healing = st.radio("Delayed Healing:", ["Yes", "No"])
partial_paresis = st.radio("Partial Paresis:", ["Yes", "No"])
muscle_stiffness = st.radio("Muscle Stiffness:", ["Yes", "No"])
alopecia = st.radio("Alopecia (Hair Loss):", ["Yes", "No"])
obesity = st.radio("Obesity:", ["Yes", "No"])

# Convert Inputs to Numeric Encoding (as per dataset)
gender = 1 if gender == "Male" else 0
polyuria = 1 if polyuria == "Yes" else 0
polydipsia = 1 if polydipsia == "Yes" else 0
sudden_weight_loss = 1 if sudden_weight_loss == "Yes" else 0
weakness = 1 if weakness == "Yes" else 0
polyphagia = 1 if polyphagia == "Yes" else 0
genital_thrush = 1 if genital_thrush == "Yes" else 0
visual_blurring = 1 if visual_blurring == "Yes" else 0
itching = 1 if itching == "Yes" else 0
irritability = 1 if irritability == "Yes" else 0
delayed_healing = 1 if delayed_healing == "Yes" else 0
partial_paresis = 1 if partial_paresis == "Yes" else 0
muscle_stiffness = 1 if muscle_stiffness == "Yes" else 0
alopecia = 1 if alopecia == "Yes" else 0
obesity = 1 if obesity == "Yes" else 0

# Scale "Age" using StandardScaler
scaled_age = scaler.transform([[age]])[0][0]  # Apply StandardScaler

# Prepare Feature Vector for Prediction
features = np.array([
    scaled_age, gender, polyuria, polydipsia, sudden_weight_loss, weakness,
    polyphagia, genital_thrush, visual_blurring, itching, irritability,
    delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity
]).reshape(1, -1)

# Prediction Button
if st.button("🔎 Predict Diabetes Risk"):
    prediction = model.predict(features)
    result = "🛑 Diabetes Detected" if prediction[0] == 1 else "✅ No Diabetes Risk"
    st.success(f"**Prediction:** {result}")
