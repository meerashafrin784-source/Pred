import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="PredictEd SignIn", layout="centered")

# --- Resolve dataset path dynamically ---
# Get the directory where this script is running (e.g., C:\PredictED\login\pages)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Dataset path in root folder
csv_path = r"C:\PredictED\student_habits_performance_with_names.csv"

# --- Load dataset safely ---
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"❌ Dataset not found at: {csv_path}")
    st.stop()

# --- Navigation Bar (visual only) ---
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
    </div>
""", unsafe_allow_html=True)

# --- Main content ---
st.markdown("""
<br><br><br>
<div class="main-content">
    <div style="width:400px; margin:auto; padding:30px; background:#fff; 
                box-shadow:0 0 15px rgba(0,0,0,0.1); border-radius:12px; text-align:center;">
        <h2 style="margin-bottom:10px;">PredictEd SignIn Portal</h2>
        <p style="font-size:14px; color:#555; margin-bottom:20px;">
            Enter your Student ID to access your dashboard
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Input field ---
sid = st.text_input("Student ID")

# --- Sign In Logic ---
if st.button("Sign In"):
    if sid.strip() == "":
        st.warning("⚠️ Please enter your Student ID.")
    elif sid in df["student_id"].astype(str).values:
        st.session_state["user_id"] = sid
        st.success("✅ ID found! Redirecting to dashboard...")
        st.switch_page("pages/student_dashboard.py")
    else:
        st.error("❌ ID not found in the dataset. Please check your input.")
