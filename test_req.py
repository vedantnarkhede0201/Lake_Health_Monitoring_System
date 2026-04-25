import requests
try:
    res = requests.post("http://localhost:8000/analyze", json={"tds": 300, "turbidity": 5, "temperature": 25, "time": "12PM"})
    print(res.status_code)
    print(res.text)
except Exception as e:
    print(e)
