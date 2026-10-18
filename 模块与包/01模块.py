# 在 Python 中，一个.py文件就是一个模块（Module）。
# 模块中可以包含：变量、函数、类、等很多内容。
# 通常把能够实现某一特定功能的代码，集中放在一个模块中（模块就类似于一个工具箱）。
# 模块可以提高代码的可维护性 与 可复用性，还可以避免命名冲突。

# Python 中的模块分为三类，分别是：标准库模块、自定义模块、第三方模块
# 模块命名注意点：

# 1.要符合标识符命名规则
# 2.模块名（.py文件名）区分大小写
# 3. 不要与标准库模块同名（一旦同名，Python会优先引入标准库模块）
# 创建如下文件：
# import order
# import pay
# print(order.max_order_amount)
# order.create_order()
# order.cancel_order()
# order.show_info()
#
# print('*' * 10)
#
# print(pay.timeout)
# pay.wechat_pay()
# pay.ali_pay()
# pay.show_info()

# import 模块名 as 别名
# import order as dingdan
# import pay as zhifu
# print(dingdan.max_order_amount)
# dingdan.create_order()
# dingdan.cancel_order()
# dingdan.show_info()
#
# print('*' * 10)
#
# print(zhifu.timeout)
# zhifu.wechat_pay()
# zhifu.ali_pay()
# zhifu.show_info()
#

# from 模块名 import 具体内容1, 具体内容2, ......
# from order import max_order_amount, show_info
# from pay import wechat_pay, ali_pay
#
# print(max_order_amount)
# show_info()
# wechat_pay()
# ali_pay()

# from 模块名 import 具体内容 as 别名
# from order import max_order_amount as max_amt, show_info as show1
# from pay import timeout as tm, show_info as show2
#
# print(max_amt)
# print(tm)
# show1()
# show2()

# from 模块名 import *,不用写order.去调用了，可以直接调用
# from order import *
# from pay import *
#
# max_order_amount = 10
#
# print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()



# __all__,__name__
# 关于__all__：
# 在 Python 模块中，可通过 __all__ 来控制from 模块 import *能导入哪些内容。
# __all__ 的值可以是：列表、元组。

# from order import*
# cancel_order()

# 关于__name__:
# __name__是每个 Python 模块（.py文件）都拥有的一个内置变量。
# 它的具体值取决于模块的运行方式：
# (1). 作为主程序直接运行，__name__ 的值是 __main__
# (2). 作为模块被导入到其他程序中运行，__name__的模块的文件名（不带.py）
import pay

