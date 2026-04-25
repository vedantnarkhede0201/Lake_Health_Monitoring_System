# 🌊 Lake Health Monitoring System

A full-stack environmental monitoring system built with Flask and React — collecting simulated IoT sensor data (TDS, Turbidity, Temperature, GPS), applying AI-based pH estimation, context-aware alerting, and water safety classification for both drinking and aquatic life.

---

## 📌 Overview

The **Lake Health Monitoring System** is an IoT-inspired application that simulates real-world lake monitoring using sensor data. It processes environmental readings, applies AI-based logic to estimate water quality parameters, and presents everything on an interactive dashboard — helping determine whether a body of water is safe for human use or aquatic life.

Built as part of a multidisciplinary academic project, the system reflects real-world environmental monitoring workflows with a focus on data integrity, intelligent alerting, and usable visualizations.

---

## ✨ Features

- **Simulated IoT Sensor Data** — Collects TDS, Turbidity, Temperature, and GPS readings
- **Scheduled Data Updates** — Data refreshes three times daily: 4 AM, 12 PM, and 8 PM
- **AI-Based pH Estimation** — Estimates pH levels using a custom ML model (no physical pH sensor required)
- **Water Safety Classification** — Determines if water is safe for drinking and/or aquatic life
- **Context-Aware Alerts** — Flags anomalies based on time of day (e.g., high temperature at 4 AM is abnormal; at noon it may not be)
- **GPS Boat Tracking** — Simulates lake-wide sensor coverage via a moving boat on an interactive map
- **Interactive Dashboard** — Real-time metrics, time-series trend graphs, and AI-generated explanations

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React (UI generated with AI assistance) |
| Backend | Python, Flask |
| Data Processing | Pandas |
| ML / Logic | Custom rule-based model + simple estimator |

---

## 📁 Project Structure

```
MDP/
├── backend/
│   ├── __pycache__/
│   ├── venv/
│   ├── ai_service.py       # AI-based pH estimation & classification logic
│   ├── main.py             # Flask API server (entry point)
│   ├── mock_data.py        # Simulated sensor data generation
│   ├── requirements.txt    # Python dependencies
│   ├── test_req.py         # Requirement/dependency tests
│   └── test_script.py      # Backend logic tests
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/                # React components & pages
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   └── vite.config.js
├── lake_data_log (1).csv   # Sensor data log
├── Lake_Training_Data_Max.csv  # ML training dataset
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- pip

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/your-username/lake-health-monitor.git
cd lake-health-monitor

# Install Python dependencies
cd backend
pip install -r requirements.txt

# Start the Flask server
python main.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:5173`.

---

## 📊 How It Works

1. **Data Simulation** — Sensor readings (TDS, Turbidity, Temperature, GPS) are generated on a schedule: 4 AM, 12 PM, and 8 PM daily.
2. **pH Estimation** — Since no physical pH sensor is used, the system estimates pH from correlated parameters using a trained model.
3. **Classification** — Rules and model outputs are combined to classify water quality for drinking and aquatic life.
4. **Alert Engine** — Alerts are evaluated against time-of-day context to reduce false positives (e.g., elevated temperature is expected at noon, not at dawn).
5. **Dashboard** — All data is surfaced on a React dashboard with live metrics, trend charts, a GPS map, and AI-generated plain-language explanations.

---

## 📸 Screenshots

### 🔢 Real-Time Sensor Metrics
![Dashboard Metrics](screenshots/dashboard_metrics.png)
> Live readings for TDS, Turbidity, Temperature, and AI-predicted pH.

### 🛡️ AI Classifications & Context-Aware Alerts
![AI Classifications and Alerts](screenshots/ai_classifications.png)
> Water safety status for drinking and aquatic life, automated explanations, and prioritized alerts.

### 🗺️ Boat GPS Tracking
![GPS Tracking](screenshots/gps_tracking.png)
> Simulated boat movement across VIT Lake, showing sensor coverage paths.

### 📈 Environmental Trends Over Time
![Environmental Trends](screenshots/env_trends.png)
> Time-series chart tracking TDS and Temperature across 3 daily readings.

---

## 🙋 Author

Developed independently as part of a 2-credit multidisciplinary group project — handling backend, data processing, AI/ML logic, and system integration end-to-end.

> The frontend UI was developed with AI assistance. It looks great. No further comments.
