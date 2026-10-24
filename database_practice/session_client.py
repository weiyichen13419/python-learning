import requests
# session = requests.Session()
# response = session.get("http://127.0.0.1:8000/set-session")
# print(response.status_code)
# print(response.json())
# cookie_value = session.cookies.get("session_id")
# print(cookie_value)
# session.cookies.clear()
# print(cookie_value)
#
#
# response = session.get("http://127.0.0.1:8000/cookie-info")
# print(response.status_code)
# print(response.json())
#
# print(session.cookies.get("not_exist"))

# response = requests.get("http://127.0.0.1:8000/cookie-info")
# print(response.status_code)
# print(response.json())

session=requests.Session()
session.cookies.set("session_id","lesson80")

response=session.get("http://127.0.0.1:8000/cookie-info")
print(response.status_code)
print(response.json())