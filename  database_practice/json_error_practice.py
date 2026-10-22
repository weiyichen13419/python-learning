
import json

json_text = '{"id": 5, "name": "王五"'

try:
    student = json.loads(json_text)
    print(student)

except json.JSONDecodeError:
    print("JSON格式错误")

print("程序继续运行")
