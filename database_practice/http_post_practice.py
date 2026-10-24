
import requests

url = "https://jsonplaceholder.typicode.com/posts"

student = {
    "title": "Python学习",
    "body": "第46课练习",
    "userId": 1
}

try:
    # 第46课：独立补全POST请求
    response = requests.post(url,json=student,timeout=10)

    response.raise_for_status()

    data = response.json()

    print(response.status_code)
    print(data.get("title"))
    print(data.get("body"))
    print(data.get("userId"))

except requests.RequestException as e:
    print("请求失败")
    print(e)
