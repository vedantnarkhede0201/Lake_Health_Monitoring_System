import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Train a dummy pH prediction model
def create_model():
    X = []
    y = []
    for _ in range(200):
        temp = np.random.uniform(5, 35)
        tds = np.random.uniform(50, 800)
        turb = np.random.uniform(0, 20)
        
        ph = 7.5 - (temp * 0.01) - (tds * 0.001) - (turb * 0.02) + np.random.normal(0, 0.1)
        ph = max(0, min(14, ph))
        
        X.append([temp, tds, turb])
        y.append(ph)
        
    model = LinearRegression()
    model.fit(X, y)
    return model

# Global singleton model for the session
ph_model = create_model()

def predict_ph(temperature, tds, turbidity):
    # Predict and format
    ph = ph_model.predict([[temperature, tds, turbidity]])[0]
    return float(round(ph, 2))

def analyze_water(timestamp_iso, temperature, tds, turbidity):
    # Predict pH
    ph = predict_ph(temperature, tds, turbidity)
    
    # 1. Classification: Drinking Water
    drinking_status = "Safe"
    if tds > 500 or turbidity > 5 or ph < 6 or ph > 9:
        drinking_status = "Not Safe"
    elif tds > 300 or turbidity > 1 or ph < 6.5 or ph > 8.5:
        drinking_status = "Moderate"
        
    # 2. Classification: Aquatic Life
    aquatic_status = "Healthy"
    if temperature > 30 or temperature < 4 or turbidity > 10 or ph < 6.0 or ph > 9.5:
        aquatic_status = "Dangerous"
    elif temperature > 25 or turbidity > 5 or ph < 6.5 or ph > 9.0:
        aquatic_status = "Risk"

    # 3. Context-Aware Intelligence (Time-based Logic) & Alerts
    dt = datetime.fromisoformat(str(timestamp_iso).replace('Z', '+00:00'))
    hour = dt.hour
    
    alerts = []
    
    # Temperature context
    if hour <= 6 or hour >= 22:
        if temperature > 20:
            alerts.append({"level": "Yellow", "message": f"Abnormal temperature ({temperature}°C) for early morning/night."})
    elif 10 <= hour <= 16:
        if temperature > 28:
            alerts.append({"level": "Yellow", "message": f"High midday temperature detected ({temperature}°C)."})
            
    if turbidity > 5:
        alerts.append({"level": "Red" if turbidity > 10 else "Yellow", "message": f"High turbidity detected ({turbidity} NTU)."})
    
    if tds > 400:
        alerts.append({"level": "Red" if tds > 600 else "Yellow", "message": f"High dissolved solids detected ({tds} ppm)."})
        
    if drinking_status == "Not Safe":
        alerts.append({"level": "Red", "message": "Water unsafe for drinking due to combined poor parameters."})

    # AI Explanations
    explanations = []
    if drinking_status == "Not Safe":
         explanations.append("Water is classified as NOT SAFE for drinking primarily due to " + ("high TDS" if tds > 500 else "high turbidity" if turbidity > 5 else "abnormal pH") + ".")
    elif drinking_status == "Moderate":
         explanations.append("Water is MODERATE for drinking; treatment is required.")
    else:
         explanations.append("Water is SAFE for drinking. Parameters indicate good quality.")
         
    if aquatic_status == "Dangerous":
         explanations.append("Conditions are DANGEROUS for aquatic life. Immediate investigation required.")
    elif aquatic_status == "Risk":
         explanations.append("Conditions pose a RISK for aquatic life (potential low dissolved oxygen).")

    if not alerts:
        alerts.append({"level": "Green", "message": "All parameters are within normal ranges."})

    return {
        "ph": ph,
        "drinking_safety": drinking_status,
        "aquatic_safety": aquatic_status,
        "alerts": alerts,
        "explanations": explanations
    }
