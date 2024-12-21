import requests

# URL до API-то
url = "http://127.0.0.1:9696/predict"

payload = {
    "age": 30,
    "job": "technician",
    "marital": "single"
}

response = requests.post(url, json=payload)

print("Response status code:", response.status_code)
print("Response JSON:", response.json())
