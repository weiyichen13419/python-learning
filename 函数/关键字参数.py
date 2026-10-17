#使用关键字参数，位置参数必须在关键字参数前

# def greet(name,gender,age,height):
#     print(f'我叫{name}，我的性别是{gender}，年龄{age}，身高{height}')
#
# #调用参数
# greet(name='魏依辰',gender='男',age=20,height=172)
# greet(age=20,height=172,name='魏依辰',gender='男')
# greet('魏依辰','男',age=20,height=172)

#/前只能用位置参数，*后只能用关键字
def greet(name,/,gender,*,age,height):
    print(f'我叫{name}，我的性别是{gender}，年龄{age}，身高{height}')
greet('魏依辰','男',age=18,height=172)

