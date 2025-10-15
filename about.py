import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="PredictEd", layout="wide")

# --- Light Bluish Background ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #cce6ff, #99ccff);  /* light bluish gradient */
        background-attachment: fixed;
    }
    .block-container {
        padding-top: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

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
        color: #0066cc;
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
        color: #0066cc;
        border: 2px solid #0066cc;
    }
    .get-started-btn {
        background-color: #3399ff;
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
            <button class="login-btn">Mentor Login</button>
            <button class="get-started-btn">Student Login</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Main Content Box ---
st.markdown("""
    <style>
    .about-box {
        background-color: rgba(255, 255, 255, 0.2);  /* soft transparent white */
        border-radius: 15px;
        padding: 50px;
        max-width: 800px;
        margin: 200px auto 60px auto;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        font-family: 'Segoe UI', sans-serif;
        color: #003366;
    }
    .about-box h1 {
        font-size: 48px;
        margin-bottom: 20px;
    }
    .about-box p {
        font-size: 18px;
        line-height: 1.6;
        color: #003366;
    }
    </style>

    <div class="about-box">
        <h1>About PredictEd</h1>
        <p>
            PredictEd is an innovative educational platform that leverages artificial intelligence to provide personalized learning insights and academic performance predictions.
            Our advanced algorithms analyze your learning patterns, attendance, and study habits to help you achieve your academic goals with data-driven recommendations.
        </p>
    </div>
""", unsafe_allow_html=True)
