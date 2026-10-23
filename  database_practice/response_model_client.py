url="http://127.0.0.1:8000/ai/chat"
import requests

response=requests.post(url,
                       json={"prompt":"你好，AI"})
print(response.status_code)
print(response.json())

response=requests.post(url,
                       json={"prompt":" Python "})
print(response.status_code)
print(response.json())

response=requests.post(url,
                       json={"prompt":"   "})
print(response.status_code)
print(response.json())

response=requests.post(url,
                       json={})
print(response.status_code)
print(response.json())