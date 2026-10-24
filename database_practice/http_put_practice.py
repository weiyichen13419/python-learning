
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

new_data = {
    "id": 1,
    "title": "Python后端开发",
    "body": "第47课PUT请求练习",
    "userId": 1
}
try:
    response = requests.put(url,json=new_data,timeout=10)

    response.raise_for_status()
    data=response.json()
    print(response.status_code)
    print(data["id"])
    print(data["title"])
    print(data["body"])
except requests.RequestException as e:
    print("请求失败")
    print(e)
