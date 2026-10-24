import requests
response=requests.get("http://127.0.0.1:8000/search", params={"keyword": "Python"})
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/search", params={"keyword": "A"})
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/search", params={"keyword": ""})
print(response.status_code)
print(response.json())