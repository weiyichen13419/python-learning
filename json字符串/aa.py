from pathlib import Path
import json
path=Path('user_info.json')
user = {}
user['name']=input('请输入姓名：')
user['age']=int(input('请输入年龄：'))
contents = json.dumps(user)
path.write_text(contents,encoding='utf-8')
print(f'信息已记录到{path}文件中')
