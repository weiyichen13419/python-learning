import requests
session=requests.Session()
session.cookies.update({"session_id":"lesson83",
                        "view_mode":"dark"})
print(session.cookies.get_dict())