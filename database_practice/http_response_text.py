import requests
try:
    response=requests.get(
        "https://example.com",
        timeout=10
    )
    print(response.status_code)
    print(response.text)
    print(type(response.text))
except requests.RequestException:
    print("网络请求失败")
