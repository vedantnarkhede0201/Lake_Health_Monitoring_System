from main import app
with app.test_client() as client:
    res = client.post('/analyze', json={"tds": 300, "turbidity": 5, "temperature": 25, "time": "12PM"})
    print(res.data)
