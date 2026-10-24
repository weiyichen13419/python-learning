import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.delete(url,timeout=10)
    response.raise_for_status()
    print(response.status_code)
    print("删除请求成功")
except requests.RequestException as e:
    print("请求失败",e)