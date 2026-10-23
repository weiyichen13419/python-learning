import requests
url="http://127.0.0.1:8000/notes"
response=requests.post(url,
            json={"content":"今天学习了FastAPI"})
print(response.status_code)
print(response.json())

response=requests.post(url,
            json={"content":"明天继续学习Python"})
print(response.status_code)
print(response.json())

response=requests.post(url,
            json={"content":""})
print(response.status_code)
print(response.json())

response=requests.post("http://127.0.0.1:8000/ai/chat",
            json={"prompt":"你好，AI"})
print(response.status_code)
print(response.json())