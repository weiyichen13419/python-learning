import json
json_text = '{"id": 2, "name": "李四"}'

student = json.loads(json_text)

if isinstance(student, dict):
    print("数据是字典")
    print(student.get("name"))
else:
    print("数据类型不正确")
print(isinstance(student, list))

import json

json_text = '[{"id": 5, "name": "王五"}]'

student = json.loads(json_text)

if isinstance(student, dict):
    print("字典")
else:
    print("不是字典")

print(isinstance(student, list))
print(type(student))