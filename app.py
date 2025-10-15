import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Get absolute path of the current script (app.py)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset path in root folder
csv_path = r"C:\PredictED\student_habits_performance_with_names.csv"
model_path = os.path.join(SCRIPT_DIR, "best_model.pkl")

# Load dataset and model
df = pd.read_csv(csv_path)
model = joblib.load(model_path)


# --- Navigation Bar (visual only, not functional links) ---
st.markdown("""
    <style>
    .nav-container {
        position: fixed;
        top: 60px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 3rem;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        font-family: 'Segoe UI', sans-serif;
        z-index: 9999;
    }
    .nav-left h2 {
        color: #6a1b9a;
        margin: 0;
        font-weight: 800;
        font-size: 28px;
    }
    </style>

    <div class="nav-container">
        <div class="nav-left">
            <h2>
                <img src="https://img.icons8.com/ios-filled/30/6a1b9a/artificial-intelligence.png">
                PredictEd
            </h2>
        </div>
""", unsafe_allow_html=True)
st.write("")
st.write("")
st.title("🎓 Student Final Score Predictor")
# --- Dashboard Header ---
st.markdown("""
    <style>
    .nav-container {
        position: fixed;
        top: 60px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 3rem;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        font-family: 'Segoe UI', sans-serif;
        z-index: 9999;
    }
    .nav-left h2 {
        color: #6a1b9a;
        margin: 0;
        font-weight: 800;
        font-size: 28px;
    }
    <div class="nav-container">
        <div class="nav-left">
            <h2>
                <img src="https://img.icons8.com/ios-filled/30/6a1b9a/artificial-intelligence.png">
                PredictEd
            </h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# Inject CSS for fully blue sliders and button
st.markdown("""
<style>
/* Entire slider track */
div[data-baseweb="slider"] > div > div {
    background: #d3d3d3;
    height: 6px;
    border-radius: 4px;
}

/* Filled portion of slider track */
div[data-baseweb="slider"] > div > div > div {
    background: #1E90FF !important;
    height: 6px;
    border-radius: 4px;
}

/* Slider thumb handle */
div[data-baseweb="slider"] span[role="slider"] {
    background-color: #1E90FF !important;
    border: 2px solid #1E90FF !important;
}

/* Slider label text */
.css-1b43r93 { color: #1E90FF !important; }

/* Button styling */
.stButton>button {
    background-color: #1E90FF;
    color: white;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #0b66c3;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ----------------- User Inputs -----------------
study_hours = st.slider("Study Hours per Day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider("Mental Health Rating (1-10)", 1, 10, 5)
sleep_hours = st.slider("Sleep Hours per Night", 0.0, 12.0, 7.0)
assignment_score = st.slider("Assignment Score (out of 10)", 0, 10, 8)
part_time_job = st.selectbox("Part-Time Job", ["No", "Yes"])

# Encode part-time job
ptj_encoded = 1 if part_time_job == "Yes" else 0

# ----------------- Prediction -----------------
if st.button("Predict Final Score"):
        # Prepare input for prediction
        input_data = np.array([[study_hours, attendance, mental_health,
                                sleep_hours, ptj_encoded, assignment_score]])
        final_score = model.predict(input_data)[0]
        final_score = max(0, min(100, final_score))  # ensure score 0-100

        # Determine risk level
        if final_score < 50:
            risk_level = "High Risk"
            color = "red"
        elif 50 <= final_score <= 70:
            risk_level = "Moderate Risk"
            color = "orange"
        else:
            risk_level = "No Risk"
            color = "green"

        # Display results
        st.markdown(f"### 🎯 Predicted Final Score: **{final_score:.2f}**")
        st.markdown(f"<p style='color:{color}; font-size:20px; font-weight:bold;'>{risk_level}</p>", unsafe_allow_html=True)

