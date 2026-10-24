import requests
response=requests.get("http://127.0.0.1:8000/header-test",
                      headers={"X-Client-Name":"PyCharm"})
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/header-test",
                      headers={"X-Client-Name":"PythonRequests"})
print(response.status_code)
print(response.json())

response=requests.get("http://127.0.0.1:8000/header-test")
print(response.status_code)
print(response.json())