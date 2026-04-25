from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import math
from datetime import datetime

def safe_float(val, default):
    try:
        f = float(val)
        if math.isnan(f):
            return default
        return f
    except Exception:
        return default

app = Flask(__name__)
CORS(app) # Enable CORS properly

LAKE_LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "lake_data_log (1).csv")

def estimate_ph(tds, turbidity, temperature):
    ph = 7.0
    ph -= (tds / 1000)
    ph -= (turbidity / 50)
    ph += (temperature - 25) * 0.02
    return round(ph, 2)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Backend is running. Use /analyze to send data."}), 200

@app.route("/analyze", methods=["GET", "POST", "OPTIONS"])
def analyze():
    if request.method == "OPTIONS":
        return jsonify({}), 200
        
    try:
        if not os.path.exists(LAKE_LOG_FILE):
            return jsonify({"error": "CSV log file not found"}), 404
            
        df = pd.read_csv(LAKE_LOG_FILE)
        if df.empty:
            return jsonify({"error": "CSV log file is empty"}), 404
            
        history_payload = []
        for _, row in df.iterrows():
            history_payload.append({
                "timestamp": str(row.get("Timestamp", "")),
                "tds": float(row.get("TDS", 0)),
                "turbidity": float(row.get("Turb", 0)),
                "temperature": float(row.get("Temp", 0)),
                "gps": {"lat": safe_float(row.get("Lat"), 39.0968), "lng": safe_float(row.get("Lon"), -120.0324)}
            })
            
        latest = df.iloc[-1]
        tds = float(latest.get("TDS", 0))
        turbidity = float(latest.get("Turb", 0))
        temperature = float(latest.get("Temp", 0))
        
        # Parse time string for anomalies
        timestamp_str = str(latest.get("Timestamp", ""))
        try:
            hour = pd.to_datetime(timestamp_str).hour
            time_str = "12PM"
            if hour < 8: time_str = "4AM"
            elif hour > 18: time_str = "8PM"
        except:
            time_str = "12PM"
        
        # Determine safety and health status using AI service
        from ai_service import analyze_water
        
        # Determine safety and health status using AI model
        analysis_result = analyze_water(timestamp_str, temperature, tds, turbidity)
        
        response_data = {
            "timestamp": timestamp_str,
            "tds": tds,
            "turbidity": turbidity,
            "temperature": temperature,
            "ph": analysis_result["ph"],
            "gps": {"lat": safe_float(latest.get("Lat"), 39.0968), "lng": safe_float(latest.get("Lon"), -120.0324)},
            "drinking_water": analysis_result["drinking_safety"],
            "aquatic_life": analysis_result["aquatic_safety"],
            "alerts": analysis_result["alerts"],
            "explanations": analysis_result["explanations"],
            "history": history_payload
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        print("Error processing request:", str(e))
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    print("Starting Flask server on port 5001...")
    app.run(debug=True, port=5001)