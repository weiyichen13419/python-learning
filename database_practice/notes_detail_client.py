import requests
url="http://127.0.0.1:8000/notes"
response=requests.post(url,
                       json={"content":"tags验证"})
print(response.status_code)
print(response.json())
new_id = response.json()["id"]

response=requests.get(f"http://127.0.0.1:8000/notes/{new_id}")
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/notes/99999")
print(response.status_code)
print(response.json())