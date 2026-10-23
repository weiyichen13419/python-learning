import requests

response = requests.post(
    "http://127.0.0.1:8000/ai/chat",
    json={"prompt": "你好，AI"}
)

print(response.status_code)
print(response.json())

response = requests.post(
    "http://127.0.0.1:8000/ai/chat",
    json={"prompt": "请解释Python字典"}
)

print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8000/ai/chat",
    json={}
)

print(response.status_code)
print(response.json())

