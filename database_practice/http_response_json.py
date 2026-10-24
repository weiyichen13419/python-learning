
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=10)

    print(response.status_code)

    # 第44课：独立补全这一行
    data = response.json()

    print(type(data))
    print(data.get("id"))
    print(data.get("title"))

except requests.RequestException:
    print("网络请求失败")
