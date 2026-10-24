import requests
url = "http://127.0.0.1:8000/feedback"
response = requests.post(url,
                         params={"message":"Hello"},
                         )
print(response.status_code)
print(response.json())

response = requests.post(url,
                         params={"message":"Python backend"},
                         )
print(response.status_code)
print(response.json())





















