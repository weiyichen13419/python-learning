import requests
response = requests.get("http://127.0.0.1:8000/set-session")
print(response.status_code)
print(response.json())

cookie=response.cookies.get("session_id")
print(cookie)
response=requests.get("http://127.0.0.1:8000/cookie-info",
                      cookies= {"session_id":cookie})
print(response.status_code)
print(response.json())
