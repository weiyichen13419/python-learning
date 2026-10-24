
import json

json_text = '{"id": 2, "name": "李四"}'

student = json.loads(json_text)


name = student.get("name")
age = student.get("age")
city = student.get("city","北京")

print(name)
print(age)
print(city)
