# def speak(msg):
#     print('-----')
#     print(msg)
#     print('-----')
#
# def greet(name,msg):
#     print(f'Hello，我叫{name},我想说的话在下面')
#     speak(msg)
#     print('我想说的结束了')
# greet('wyc','hello')





# def greet(name,msg):
#     print(f'Hello，我叫{name},我想说的话在下面')
#     speak(msg)
#     print('我想说的结束了')
#
# def speak(msg):
#     print('-----')
#     print(msg)
#     print('-----')
#
#
# greet('wyc','hello')



def test1():
    print('进入test1函数')
    test2()
    print('退出test1函数')

def test2():
    print('进入test2函数')
    test3()
    print('退出test2函数')

def test3():
    print('进入test3函数')
    print('***正在执行test3函数***')
    print('退出test3函数')
test1()