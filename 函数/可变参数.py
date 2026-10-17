#可变位置参数，前加*
# def test1(*args):
#     #此处args的输出为元组
#     print(args)
# test1('wyc','male',18,172)
#
# #  **可变关键字参数
# def test2(**kwargs):
#     # 此处kwargs的输出为字典
#     print(kwargs)
# test2(name='wyc',gender='male',age=18,height=172)

#可以同时用，但必须先用可变位置。也可以和其它类型参数一起使用
def test3(a,b,*args,c='iron',**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)

test3('wyc','male','打游戏','看小说',c='bro',age=18,height=172)

