import requests

response=requests.delete("http://127.0.0.1:8000/notes/11")
print(response.status_code)
print(response.json())
