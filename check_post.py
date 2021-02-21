import requests
import json


url = 'http://localhost:8000/api/v1/goods/4/reviews/'
data = {
    "text": "Best. Cheese. Ever.",
    "grade": "8"
    }
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url=url, json=data, headers=headers)
print(response.text)
print(response.status_code)