# import requests
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


# response = session.get("http://127.0.0.1:8000/set-session")
# print(response.status_code)
# print(response.json())
# print(session.cookies.get_dict())
#
# session=requests.Session()
# session.cookies.set("session_id","lesson82")
# session.cookies.set("view_mode","dark")
# print(session.cookies.get_dict())
# session.cookies.pop("session_id",None)
# print(session.cookies.get_dict())
#


import requests
session=requests.Session()
session.headers.update(
    {"X-Client-Name":"PythonLesson84"}
)
print(session.headers.get("X-Client-Name"))
