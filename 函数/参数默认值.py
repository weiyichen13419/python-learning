#可选参数，默认参数必须放在必选参数后面
def greet(name,gender,age,height,msg='你好'):
    print(f'我叫{name}，我的性别是{gender}，年龄{age}，身高{height}')
    print(f'我想说{msg}')
# greet('魏依辰','男',age=18,height=172)
greet('魏依辰','男',18,172,msg='hello')
