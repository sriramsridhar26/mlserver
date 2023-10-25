import requests

url = 'http://localhost:5000/updatevital'  # Replace with your actual endpoint URL
data = {'userid': 2, 'heartrate': 20}  # Example integer values

response = requests.post(url, json=data)

print(response.json())