import requests

url = "http://localhost/predict"
payload = {"age": 30, "job": "technician", "marital": "single"}

response = requests.post(url, json=payload)

print("Response status code:", response.status_code)
print("Response JSON:", response.json())
