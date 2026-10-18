import json
from pathlib import Path

path = Path('user_info.json')
contents = path.read_text()
user = json.loads(contents)
print(f'欢迎回来{user['name']}')
print(f'你的年龄是：{user['age']}')
