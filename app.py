import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("stress_predictor_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.set_page_config(page_title="Student Stress Predictor", layout="centered")
st.title("🎓 Student Stress Level Predictor")
st.markdown("Enter your lifestyle details to predict your stress level.")

# User Inputs
study_hours = st.slider("📚 Study Hours per Day", 0, 12, 4)
extracurricular_hours = st.slider("🎨 Extracurricular Hours", 0, 6, 2)
sleep_hours = st.slider("😴 Sleep Hours per Day", 0, 12, 7)
social_hours = st.slider("🗣️ Social Hours per Day", 0, 6, 2)
physical_activity = st.slider("🏃‍♀️ Physical Activity Hours", 0, 6, 1)
gpa = st.slider("📊 GPA (0.0 to 4.0)", 0.0, 4.0, 3.2, step=0.01)

# Combine input into a feature array
features = np.array([[study_hours, extracurricular_hours, sleep_hours,
                      social_hours, physical_activity, gpa]])

# Predict button
if st.button("🎯 Predict Stress Level"):
    prediction = model.predict(features)[0]
    label = {0: "High", 1: "Low", 2: "Moderate"}[prediction]
    st.success(f"Predicted Stress Level: **{label}**")

