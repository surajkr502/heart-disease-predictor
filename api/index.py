#Import Libraries
from dataclasses import field
import os
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse

# Make FastAPI App 
app = FastAPI(title="Heart Disease Predictor")



# Load Path and Models 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "heart_model.joblib")
model = joblib.load(MODEL_PATH)

# Home route
@app.get("/")
def home():
    return FileResponse(os.path.join(BASE_DIR, "..", "public", "index.html"))

# Input Schema (Pydantic Model)
class Patient(BaseModel):
    Age: int = Field(..., ge=1, le=120)
    Sex: str = Field(..., description="1 for Male, 0 for Female")
    ChestPainType: str = Field(..., description="Typical Angina, Atypical Angina, Non-Anginal Pain, Asymptomatic")
    RestingBP: float = Field(..., ge=0)
    Cholesterol: float = Field(..., ge=0)
    FastingBS: int = Field(..., ge=0, le=1)
    RestingECG: str = Field(..., description="Normal, ST-T Abnormality, Left Ventricular Hypertrophy")
    MaxHR: int = Field(..., ge=0)
    ExerciseAngina: str = Field(..., description="Yes or No")
    Oldpeak: float = Field(..., ge=0)
    ST_Slope: str = Field(..., description="Up, Flat, Down")

# Home route

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Main prediction route

@app.post("/api/predict")
def predict(patient: Patient):
    df = pd.DataFrame([patient.model_dump()])  # Create a DataFrame from the input data

    prob = float(model.predict_proba(df)[0, 1])
    return {
        "heart_disease_probability": round(prob, 4),
        "prediction": int(prob >= 0.5),
        "disclaimer": "This is for educational purposes only and does not constitute medical advice."
    }