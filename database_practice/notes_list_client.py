import requests
url="http://127.0.0.1:8000/notes"

response=requests.get(url)
print(response.status_code)
print(response.json())

response=requests.post(url,
                      json={"content":"学习FastAPI"})
print(response.status_code)
print(response.json())

response=requests.post(url,
                      json={"content":"学习Python"})
print(response.status_code)
print(response.json())

response=requests.get(url)
print(response.status_code)
print(response.json())
