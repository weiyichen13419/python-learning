import requests
url = "https://jsonplaceholder.typicode.com/todos/999999"

try:
    response = requests.get(url,timeout=10)
    print(response.status_code)
    response.raise_for_status()
    print("请求成功")
except requests.RequestException:
    print("请求失败")
print("程序继续运行")