import random
from datetime import datetime, timedelta

# Lake Coordinates (e.g., Lake Tahoe area roughly)
BASE_LAT = 39.0968
BASE_LNG = -120.0324

def generate_reading(timestamp: datetime, is_anomaly=False):
    hour = timestamp.hour
    
    # Baseline depending on time of day
    if hour == 4:
        temp = random.uniform(10, 14)
    elif hour == 12:
        temp = random.uniform(18, 25)
    elif hour == 20: # 8 PM
        temp = random.uniform(15, 19)
    else:
        temp = random.uniform(14, 20)
        
    tds = random.uniform(100, 300)
    turbidity = random.uniform(0.5, 3.0)
    
    if is_anomaly:
        anomaly_type = random.choice(['high_temp', 'high_tds', 'high_turbidity'])
        if anomaly_type == 'high_temp':
            temp += random.uniform(8, 12)
        elif anomaly_type == 'high_tds':
            tds = random.uniform(550, 800)
        elif anomaly_type == 'high_turbidity':
            turbidity = random.uniform(8.0, 15.0)

    # Random movement for boat
    lat = BASE_LAT + random.uniform(-0.02, 0.02)
    lng = BASE_LNG + random.uniform(-0.02, 0.02)

    return {
        "timestamp": timestamp.isoformat(),
        "temperature": round(temp, 2),
        "tds": round(tds, 2),
        "turbidity": round(turbidity, 2),
        "gps": {"lat": lat, "lng": lng}
    }

def generate_history(days=7):
    history = []
    now = datetime.now()
    # Normalize to midnight
    base_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    for day in range(days):
        current_date = base_date - timedelta(days=days-day)
        
        for hour in [4, 12, 20]:
            reading_time = current_date.replace(hour=hour)
            # Maybe 5% chance of historical anomaly
            is_anomaly = random.random() < 0.05
            history.append(generate_reading(reading_time, is_anomaly))
            
    return history

def get_current_reading():
    # To demonstrate anomalies efficiently for the UI, let's have a higher anomaly chance (20%)
    is_anomaly = random.random() < 0.2
    return generate_reading(datetime.now(), is_anomaly)
