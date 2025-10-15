import pandas as pd
import numpy as np
import joblib
import os

# --- Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(SCRIPT_DIR, "best_model.pkl")

# Use a raw string for Windows path to avoid escape issues
csv_path = r"C:\PredictED\student_habits_performance_with_names.csv"

# --- Load dataset and model ---
df = pd.read_csv(csv_path)
model = joblib.load(model_path)

# --- Encode part-time job ---
df["part_time_job_encoded"] = df["part_time_job"].apply(lambda x: 1 if x == "Yes" else 0)

# --- Features used for prediction ---
features = [
    "study_hours_per_day",
    "attendance_percentage",
    "mental_health_rating",
    "sleep_hours",
    "part_time_job_encoded",
    "Assignment_Score"
]

# --- Predict final scores ---
X = df[features].values
df["Final_Score"] = model.predict(X).clip(0, 100)

# --- Compute risk level ---
def get_risk_level(score):
    if score < 50:
        return "High Risk"
    elif score <= 70:
        return "Moderate Risk"
    else:
        return "No Risk"

df["Risk_Level"] = df["Final_Score"].apply(get_risk_level)

# --- Save updated CSV back to the same path ---
df.to_csv(csv_path, index=False)
print("✅ Scores & risk levels updated for all students!")
