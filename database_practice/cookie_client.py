import requests
response=requests.get("http://127.0.0.1:8000/cookie-info",
                      cookies={"session_id":"abc123"})
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/cookie-info",
                      cookies={"session_id":"python456"})
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/cookie-info")
print(response.status_code)
print(response.json())