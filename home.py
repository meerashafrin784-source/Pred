import streamlit as st
import base64
import os

# --- Page Config ---
st.set_page_config(page_title="PredictEd", layout="wide")

# --- Background Image ---
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/png;base64,{encoded}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("image.png")

# --- Initialize navigation state ---
if "navigate_to" not in st.session_state:
    st.session_state.navigate_to = None

# --- Hidden buttons for navigation ---
if st.button("student_signin_hidden", key="student_hidden"):
    st.session_state.navigate_to = "student_signin"
    st.experimental_rerun()

if st.button("mentor_signin_hidden", key="mentor_hidden"):
    st.session_state.navigate_to = "mentor_signin"
    st.experimental_rerun()

# --- Detect navigation ---
if st.session_state.navigate_to == "student_signin":
    import student_signin  # loads student_signin.py
elif st.session_state.navigate_to == "mentor_signin":
    import mentor_signin  # loads mentor_signin.py

# --- Navigation Bar ---
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
    .nav-right button {
        margin-left: 1rem;
        padding: 0.5rem 1.2rem;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        cursor: pointer;
        font-size: 15px;
    }
    .login-btn {
        background-color: white;
        color: #4a90e2;
        border: 2px solid #4a90e2;
    }
    .get-started-btn {
        background-color: #6a1b9a;
        color: white;
    }
    </style>

    <div class="nav-container">
        <div class="nav-left">
            <h2>
                <img src="https://img.icons8.com/ios-filled/30/6a1b9a/artificial-intelligence.png">
                PredictEd
            </h2>
        </div>
        <div class="nav-right">
            <button class="login-btn" onclick="document.querySelector('button[kind=primary]').click();">
                Mentor Login
            </button>
            <button class="get-started-btn" onclick="document.querySelector('button[key=student_hidden]').click();">
                Student Login
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Main Content ---
st.markdown("""
    <style>
    .frosted-box {
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 15px;
        padding: 40px;
        max-width: 700px;
        margin: 120px auto 60px auto;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>

    <div class="frosted-box">
        <h1 style="font-size: 60px; color: #6a1b9a;">PredictEd</h1>
        <h3 style="color: #333;">AI-Driven Educational Forecasting</h3>
        <p style="font-size: 18px; color: #444;">
            Empowering students through data-driven insights to help each one perform.
        </p>
        <div style="margin-top: 30px;">
            <button style="padding: 10px 20px; background-color: #6a1b9a; color: white; border: none; border-radius: 5px; font-weight: bold; margin-right: 10px;"
                onclick="document.querySelector('button[key=student_hidden]').click();">
                Student Login
            </button>
            <button style="padding: 10px 20px; background-color: white; color: #333; border: 2px solid #333; border-radius: 5px; font-weight: bold;"
                onclick="document.querySelector('button[kind=primary]').click();">
                Mentor Login
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)
