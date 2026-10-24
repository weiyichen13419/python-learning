
import requests

url = "https://example.com"

try:

    response = requests.get(url,timeout=10)

    print(response.status_code)
    
except requests.RequestException:
    print("网络请求失败")
