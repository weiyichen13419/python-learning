
import json

json_text = '{"id": 2, "name": "李四"}'

# 请独立补全这一行
student = json.loads(json_text)

print(student)
print(type(student))
print(type(json_text))
print(student["name"])
