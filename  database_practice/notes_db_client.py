import requests

url="http://127.0.0.1:8000/notes"
response=requests.post(url,
                      json={"content":"第一条SQLite笔记"})
print(response.status_code)
print(response.text)

response=requests.post(url,
                      json={"content":"第二条SQLite笔记"})
print(response.status_code)
print(response.text)

response=requests.get(url)
print(response.status_code)
print(response.text)

response=requests.post(url,
                      json={"content":""})
print(response.status_code)
print(response.text)