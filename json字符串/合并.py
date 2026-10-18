import json
from pathlib import Path
path = Path('user_info.json')
#如果文件存在-读取，并转为变量
if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
    print(f'欢迎回来{user['name']}')
    print(f'你的年龄是：{user['age']}')
#如果不存在——写入
else:
    user = {}
    user['name']=input('请输入姓名：')
    user['age']=int(input('请输入年龄：'))
    contents = json.dumps(user)
    path.write_text(contents,encoding='utf-8')
    print(f'信息已记录到{path}文件中')

