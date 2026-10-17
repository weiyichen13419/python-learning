def test(*args):
    print(f'我是test函数，我收到的参数是：{args},我的类型是：{type(args)}')

list1=[100,200,300,400]
tuple1=('hello','world')
test(*list1)
test(*tuple1)

test(1,2,3,4,5)

