import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="PredictEd Dashboard", layout="wide")

# --- Load dataset ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Dataset path in root folder
csv_path = r"C:\PredictED\student_habits_performance_with_names.csv"

# --- Load dataset safely ---
df = pd.read_csv(csv_path)
# --- Check if student_id exists in session_state ---
if "user_id" in st.session_state:
    student_id = st.session_state["user_id"]
    
    # Check if student_id exists in the dataset
    if student_id in df["student_id"].values:
        student_name = df.loc[df["student_id"] == student_id, "student_name"].values[0]
        predicted_score = df.loc[df["student_id"] == student_id, "Final_Score"].values[0]
        attendance_rate = df.loc[df["student_id"] == student_id, "attendance_percentage"].values[0]
    else:
        st.error("Student ID not found in the dataset.")
        st.stop()

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
    # --- Dashboard Header with Student Details ---
    st.markdown(f"""

<style>
    .student-name {{
        text-align: center;
        color: #6a1b9a;
        font-weight: 800;
        font-size: 36px;
        margin-top: 40px;
        margin-bottom: 40px;
                
    }}
    .student-cards {{
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
    }}
    .student-card {{
        background-color: #f9f9f9;
        border-radius: 15px;
        padding: 20px 30px;
        width: 250px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }}
    .student-card:hover {{
        transform: scale(1.05);
        border: 2px solid #6a1b9a;
    }}
    .student-card p {{
        font-size: 16px;
        color: #333;
        margin: 6px 0;
    }}
</style>

<div class="student-name">Welcome, {student_name}! 👋</div>

<div class="student-cards">
    <div class="student-card">
        <p><strong>Student ID</strong></p>
        <p>{student_id}</p>
    </div>
    <div class="student-card">
        <p><strong>Predicted Score</strong></p>
        <p>{predicted_score}%</p>
    </div>
    <div class="student-card">
        <p><strong>Attendance Rate</strong></p>
        <p>{attendance_rate}%</p>
    </div>
</div>
""", unsafe_allow_html=True)

    # --- Features Section ---
    st.markdown("""
        <h2 style = {font-weight : bold; font-size : 5px}> Your Learning Insights </h2>
        <style>
        .features-row { display: flex; justify-content: center; gap: 40px; margin-top: 60px; flex-wrap: wrap; }
        .feature-card { background-color: #f9f9f9; border-radius: 15px; padding: 30px; width: 300px;
                        text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); transition: transform 0.2s ease; }
        .feature-card:hover { transform: scale(1.03); border: 2px solid #6a1b9a; }
        .feature-card img { margin-bottom: 15px; }
        .feature-card h3 { font-size: 22px; margin-bottom: 10px; color: #6a1b9a; }
        .feature-card p { font-size: 15px; color: #444; }
        </style>

        <div class="features-row">
            <div class="feature-card">
                <a href="/app">
                    <img src="https://img.icons8.com/ios-filled/50/6a1b9a/artificial-intelligence.png"/>
                    <h3>AI Predictions</h3>
                    <p>Forecast academic performance using smart algorithms.</p>
                </a>
            </div>
            <div class="feature-card">
                <img src="https://img.icons8.com/ios-filled/50/6a1b9a/combo-chart.png"/>
                <h3>Learning Analytics</h3>
                <p>Track study habits and learning efficiency.</p>
            </div>
            <div class="feature-card">
                <img src="https://img.icons8.com/ios-filled/50/6a1b9a/line-chart.png"/>
                <h3>Performance Tracking</h3>
                <p>Visualize progress with charts and trends.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- Logout Button ---
    if st.button("Logout"):
        st.session_state.pop("user_id")  # match the session_state key
        st.experimental_rerun()

else:
    st.warning("Please go to the SignIn page and enter your Student ID first.")
