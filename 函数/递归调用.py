# def welcome(n):
#     print(f'hello world{n}')
#     if n > 1:
#         welcome(n - 1)
#
# welcome(5)

#下面这段可以从1到5，栈原理，5放在最后输出了
#先递归后打印，（先下潜再打印
def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'hello world{n}')


welcome(5)
