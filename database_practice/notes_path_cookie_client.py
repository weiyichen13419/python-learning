import requests
response=requests.get("http://127.0.0.1:8000/set-notes-path-cookie")
print(response.status_code)
print(response.json())
print(response.headers.get("Set-Cookie"))